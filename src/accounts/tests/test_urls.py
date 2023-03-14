from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import UserRegisterView

from accounts.views import user_profile_view, user_activate


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, user_profile_view)

    def test_activate_user_url_resolves(self):
        url = reverse('accounts:register_activate', kwargs={'sign': 'ewsad'})
        self.assertEqual(resolve(url).func, user_activate)

