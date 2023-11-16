from django.urls import path
from core.api.views import add_appointment, get_departments, get_doctors

app_name = 'core_api'

urlpatterns = [
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('departments/', get_departments, name='get_departments'),
    path('doctors/', get_doctors, name='get_doctors'),
]