import os
from django.conf import settings
from django.core.management.base import BaseCommand
import json
from faker import Faker


POSITION_CHOICES = ['СЕО', 'Middle', 'Junior', 'Senior', 'QA']

class Command(BaseCommand):
    help = 'create data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker(['ru_RU'])
        persons = []
        # for i in range(1, 500001):
        for i in range(1, total):
            id = i
            fields = dict()
            person = dict(model="staff.employee", pk=id, fields=fields)
            name = fake.name()
            position = fake.random_element(POSITION_CHOICES)
            salary = fake.random_int(min=500, max=5000, step=50)
            employment_date = fake.date()
            chief = fake.random_int(min=1, max=total)
            level = fake.random_int(min=1, max=5)
            fields['name'] = name
            fields['position'] = position
            fields['salary'] = salary
            fields['employment_date'] = employment_date
            fields['chief'] = chief
            fields['level'] = level
            persons.append(person)
            with open('staff/fixtures/data.json', 'w+') as f:
                json.dump(persons, f)
        print(persons)
        #     # with open('staff/fixtures/data.json', 'w+') as f:
        #     #     json.dump(persons, f)
