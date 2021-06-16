from django.shortcuts import render

# Create your views here.
from staff.employee.models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employee_list": employees}
    return render(request, 'employee/employee_list.html', context)