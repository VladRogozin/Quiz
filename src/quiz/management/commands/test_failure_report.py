from datetime import datetime, time, timedelta

from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from prettytable import PrettyTable

from quiz.models import Result


class Command(BaseCommand):

    def handle(self, *args, **options):
        start = make_aware(datetime.combine(timezone.now(), time()))
        end = make_aware(datetime.combine(timezone.now() + timedelta(1), time()))

        results = Result.objects.filter(update_timestamp__range=(start, end), state=0)
        if results:
            for result in results:
                user = result.user
                tab = PrettyTable()
                tab.field_names = ['Username', 'Test', 'Duration']
                tab.add_row([
                    result.user.username,
                    result.exam.title,
                    f'{result.create_timestamp}'
                ])
                subj = f"Report from {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}"
                send_mail(subject=subj, message=tab.get_string(), from_email=None, recipient_list=[user.email])
                self.stdout.write("The report was sent by the admin's email.")
        else:
            self.stdout.write("Nothing to send.")

