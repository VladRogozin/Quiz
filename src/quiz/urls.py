from django.urls import path
from django.views.generic import TemplateView

from .views import ExamDetailView
from .views import ExamListView
from .views import ExamResultCreateView
from .views import ExamResultQuestionView

app_name = 'quiz'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    path('<uuid:uuid>/result/create/', ExamResultCreateView.as_view(), name='result_create'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/question/<int:order_num>/',
         ExamResultQuestionView.as_view(), name='question'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/details/',
         TemplateView.as_view(template_name='results/details.html'), name='result_details'),
]
