from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_id = models.IntegerField(unique=True)
    emp_email = models.EmailField(unique=True)
