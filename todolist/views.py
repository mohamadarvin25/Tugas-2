from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

from todolist.forms import CreateTaskForm
from todolist.models import ToDoList

# Create your views here.


def show_create_task(request):
    form = CreateTaskForm()
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()
        if form.is_valid():
            form.save()
            return redirect('todolist:show_todolist')
    context = {
        'page_title': 'Task Baru',
        'form': form,
    }
    return render(request, "create-task.html", context)


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = ToDoList.objects.filter(user=request.user)
    context = {
    'tasks': data_todolist,
    'nama': request.user,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)


def register(request):
    form=UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context={'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response=HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context={}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response=HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def hapus_task(request, task_id):
    deleted_item = ToDoList.objects.get(pk=task_id)
    deleted_item.delete()
    return redirect('todolist:show_todolist')

def update_task(request, task_id):
    updated_task = ToDoList.objects.get(pk=task_id)
    if updated_task.is_finished:
        updated_task.is_finished = False
    else:
        updated_task.is_finished = True
    updated_task.save()
    return redirect('todolist:show_todolist')
