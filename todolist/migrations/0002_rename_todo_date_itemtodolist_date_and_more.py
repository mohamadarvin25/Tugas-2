# Generated by Django 4.1 on 2022-09-27 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtodolist',
            old_name='todo_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='itemtodolist',
            old_name='todo_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='itemtodolist',
            old_name='todo_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='itemtodolist',
            old_name='todo_user',
            new_name='user',
        ),
    ]
