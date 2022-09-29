from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User,blank = True,null =True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.title
