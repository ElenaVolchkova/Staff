# Django:
from django.urls import path

# Localfolder:
from .views import employee_list

app_name = "employee"
urlpatterns = [
    path("", employee_list, name="employee-list"),
]