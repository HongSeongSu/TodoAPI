# Generated by Django 2.1.3 on 2018-12-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '중요'), ('2', '보통'), ('3', '사소')], default='2', max_length=1),
        ),
    ]
