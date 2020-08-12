from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import Case, Task
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import redirect


def index(request):
    template = loader.get_template('index.html')
    cases = Case.objects.order_by('-create_date')
    tasks = Task.objects.all()

    context = {
        'cases': cases,
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))


def edit_case(request):
    case_id = request.GET.get('id')
    case_name = request.GET.get('name')
    case_desc = request.GET.get('desc')
    if case_id is not None:
        case = Case.objects.filter(case_id=case_id)[0]
        case.fio = case_name
        case.description = case_desc
        case.save()
        return HttpResponseRedirect('/crm/')
    return HttpResponse('/crm/')


def create_task(request):
    if request.method == 'GET':
        id_case = request.GET.get('id_case')
        case = Case.objects.filter(case_id=id_case)[0]
        context = {
            'case': case
        }
        template = loader.get_template('createTask.html')
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        id_case = request.GET.get('id')
        name = request.GET.get('name')
        desc = request.GET.get('desc')
        cmd = request.GET.get('cmd')
        date = request.GET.get('date')
        task = Task()
        task.task_name = name
        task.task_desc = desc
        task.priority = cmd
        task.work_date = date
        task.create_date = datetime.today()
        task.user_cr = User.objects.all()[0]
        task.user_wr = User.objects.all()[0]
        task.status = "Не выполнена"
        task.case = Case.objects.all().filter(case_id=id_case)[0]
        task.save()
        return HttpResponseRedirect('/')


def delete_task(request):
    if request.method == 'POST':
        task_id = request.GET.get('task_id')
        task = Task.objects.all().filter(task_id=task_id)
        task.delete()
        return redirect('admin/')


def login(request):
    return HttpResponse('/login')


def logout(request):
    return HttpResponse('Logout')