from django.db import models

# Create your models here.
class Employee(models.Model):
    PRIORITIES = [('H', 'High'), ('M', "Medium"), ('L', 'Low')]
    name = models.CharField(max_length=25)
    priority = models.CharField(max_length=1, verbose_name='Learning Priorities', choices=PRIORITIES, default='M')

    def __str__(self):
        return self.name

class Division(models.Model):
    div_name = models.CharField(max_length=25)
    in_scope = models.BooleanField(help_text='If the division is target for the learning program, check this field')

    def __str__(self):
        return f'{self.id}-{self.div_name}'