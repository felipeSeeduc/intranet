# Generated by Django 4.2.7 on 2023-11-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_tarefa_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='log',
            field=models.TextField(default=''),
        ),
    ]
