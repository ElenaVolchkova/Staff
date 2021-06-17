from django.shortcuts import render

# Create your views here.
from staff.employee.models import Employee


def employee_list(request):
    employees = Employee.objects.order_by('-level').all()
    staff5 = Employee.objects.filter(level=5)
    for i in staff5:
        personal = Employee.objects.filter(chief_id=i.id)
        for item in personal:
            people = Employee.objects.filter(chief_id=item.id)
            for numero in people:
                numeros = Employee.objects.filter(chief_id=numero.id)
                for emp_e in numeros:
                    emp_es = Employee.objects.filter(chief_id=emp_e.id)
    context = {"employee_list": employees, 'staff5': staff5, 'personal': personal, 'people': people, 'numeros': numeros,
              'emp_es': emp_es}
    # import pdb; pdb.set_trace()
    return render(request, 'employee/employee_list.html', context)
