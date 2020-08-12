from django.contrib import admin
from .models import Case, Task
# Register your models here.

admin.site.register(Task)
admin.site.register(Case)