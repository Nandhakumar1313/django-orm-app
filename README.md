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


class Student(models.Model):
    referencenumber=models.CharField(primary_key=true,max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()


class StudentAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email')

admin.py

from django.contrib import admin
from myapp.models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)


```

## OUTPUT
### SERVER OUTPUT
![Screenshot (42)](https://user-images.githubusercontent.com/120230694/230915723-de20f843-c043-4938-ace2-a6ba3fca7a3a.png)

### CLIENT OUTPUT
![Screenshot (41)](https://user-images.githubusercontent.com/120230694/230916021-897c2327-ce84-4820-b7ae-ee3971bad99c.png)






## RESULT
Program executed successfully.
