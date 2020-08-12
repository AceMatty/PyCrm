from django.db import models
from django.contrib.auth.models import User


class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    create_date = models.DateField('Дата создания')
    files = models.CharField(max_length=1000)

    def __str__(self):
        return self.fio


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=600)
    priority = models.CharField(choices=[('Низкий', 'Низкий'), ('Средний', 'Средний'), ('Высокий', 'Высокий')],
                                max_length=50)
    user_cr = models.ForeignKey(User, default='', on_delete=models.CASCADE, related_name='user_create')
    user_wr = models.ForeignKey(User, default='', on_delete=models.CASCADE, related_name='user_workmen')
    create_date = models.DateField('Дата создания')
    work_date = models.DateField('Дата исполнения')
    status = models.CharField(choices=[('Выполнена', 'Выполнена'), ('Не выполнена', 'Не выполнена')], max_length=50)
    case = models.ForeignKey(Case, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
