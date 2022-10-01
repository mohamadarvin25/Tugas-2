from cgitb import text
from django import forms

from todolist.models import ToDoList


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = {'title', 'description'}
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
