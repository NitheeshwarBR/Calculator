# Generated by Django 4.1.2 on 2022-11-05 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='Firstname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='Lastname',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='Password1',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='Password2',
            new_name='pass2',
        ),
    ]