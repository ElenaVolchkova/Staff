from django.db import models

# Create your models here.
class Employee(models.Model):
    СЕО = 'СЕО'
    MIDDLE = 'MD'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    QA = 'QA'
    POSITION_CHOICES = [
        (СЕО, 'СЕО'),
        (MIDDLE, 'Middle'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (QA, 'QA'),
    ]
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        default=JUNIOR,
        verbose_name='Должность')
    name = models.CharField(max_length=200, verbose_name='ФИО')
    salary = models.FloatField(verbose_name='Зарплата')
    employment_date = models.DateField(null=True, blank=True, verbose_name='Дата приема на работу')
    chief = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, blank=True, null=True, default=None,
                              verbose_name='Начальник')
    level = models.IntegerField(default=0, verbose_name='Уровень')


    def __str__(self):
        return self.name