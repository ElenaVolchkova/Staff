import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand
import json

from django.db.models import Q
from faker import Faker

from staff.employee.models import Employee

# POSITION_CHOICES = ['СЕО', 'Middle', 'Junior', 'Senior', 'QA']

class Command(BaseCommand):
    help = 'create data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker(['ru_RU'])
        persons = []
        ids = []
        employees = []
        # for i in range(1, 500001):
        for i in range(1, total):
            id = i
            ids.append(id)
            fields = dict()
            person = dict(model="employee.employee", pk=id, fields=fields)
            name = fake.name()
            position = fake.random_element(Employee.POSITION_CHOICES)
            salary = fake.random_int(min=500, max=5000, step=50)
            employment_date = fake.date()
            # chief = fake.random_int(min=1, max=total)
            chief = fake.random_element(elements=ids)
            level = fake.random_int(min=1, max=5)
            fields['name'] = name
            fields['position'] = position
            fields['salary'] = salary
            fields['employment_date'] = employment_date
            fields['chief'] = chief
            fields['level'] = level
            persons.append(person)
            employees.append(
                Employee(name=name, position=position[0], salary=salary, employment_date=employment_date,
                         level=level))
        Employee.objects.bulk_create(employees)
        employees_n = Employee.objects.all()
        for employee in employees_n:
            if employee.level != 5:
                employee.chief = random.choice(employees_n) # Изменить choice. Ограничение на выбор chief
                employee.save()
            else:
                employee.chief = None  # Изменить choice. Ограничение на выбор chief
                employee.save()
        # print(employees)
        # print(persons)
