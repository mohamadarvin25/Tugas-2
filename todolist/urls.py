from django.urls import path
from todolist import views
from todolist.views import register, login_user, logout_user, show_todolist,show_create_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', show_create_task, name='show_create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),

]