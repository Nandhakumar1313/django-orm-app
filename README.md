# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from github.

### STEP 2:
Create a new app.

### STEP 3:
Enter the code for admin.py and models.py

### step 4:
Create django app and add employee details.


## PROGRAM

```python
models.py 

from django.db import models
from django.contrib import admin


class Employee(models.Model):
    referencenumber=models.CharField(max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email')

admin.py

from django.contrib import admin
from myapp.models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)


```

## OUTPUT

![output](./ormoutput.png)


## RESULT
Program executed successfully.
