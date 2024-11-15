# Generated by Django 4.1.7 on 2024-11-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0003_division_in_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1, verbose_name='Learning Priorities'),
        ),
    ]