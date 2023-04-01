from django.db import models
from django.contrib import admin


# Create your models here.
class Employee(models.Model):
    referencenumber=models.CharField(max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email')

