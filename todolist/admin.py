from django.contrib import admin



# Register your models here.
from todolist.models import ToDoList

admin.site.register(ToDoList)