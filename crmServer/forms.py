from django import forms

#
# class CreateTaskForm(forms.Form):
#     task_name = forms.CharField(max_length=100)
#     task_desc = forms.Textarea()
#     priority = forms.CharField(choices=[('Низкий', 'Низкий'), ('Средний', 'Средний'), ('Высокий', 'Высокий')])
#     user_cr = forms.IntegerField(default='', related_name='user_create')
#     user_wr = forms.IntegerField(default='', related_name='user_workmen')
#     create_date = forms.DateTimeField()
#     work_date = forms.DateTimeField()
#     status = forms.CharField(choices=[('Выполнена', 'Выполнена'), ('Не выполнена', 'Не выполнена')], max_length=50)
#     case = forms.CharField()
