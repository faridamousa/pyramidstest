# Generated by Django 5.1.3 on 2024-11-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='refillrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
