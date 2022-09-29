from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

from todolist.forms import CreateTask
from todolist.models import ToDoList

# Create your views here.


def show_create_task(request):
    create_task = CreateTask()
    form = CreateTask(request.POST)
    if form.is_valid():
        if request.method == "POST":
            post = form.save(commit=False)
            ToDoList.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
            )

    context = {
        'page_title': 'Task Baru',
        'create_task': create_task
    }
    return render(request, "create-task.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist = ToDoList.objects.all()
    context = {
        'tasks': todolist,
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
