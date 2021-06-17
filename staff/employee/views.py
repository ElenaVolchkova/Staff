from django.shortcuts import render

# Create your views here.
from staff.employee.models import Employee


def employee_list(request):
    # employees = Employee.objects.all().order_by('-level')
    employees = Employee.objects.order_by('-level').all()
    staff5 = Employee.objects.filter(level=5)
    # staff1 = Employee.objects.filter(level=1)
    for i in staff5:
        personal = Employee.objects.filter(chief_id=i.id)
        print(personal, "%%")
        for item in personal:
            people = Employee.objects.filter(chief_id=item.id)
            print(people, "//")
            for numero in people:
                numeros = Employee.objects.filter(chief_id=numero.id)
                print(numeros, "**")
                for emp_e in numeros:
                    emp_es = Employee.objects.filter(chief_id=emp_e.id)

    context = {"employee_list": employees, 'staff5': staff5, 'personal': personal, 'people': people, 'numeros': numeros,
              'emp_es': emp_es}
    # import pdb; pdb.set_trace()
    return render(request, 'employee/employee_list.html', context)
