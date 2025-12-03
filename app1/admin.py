from django.contrib import admin
from app1.models import Employee

class Employee_admin(admin.ModelAdmin):
    list_display = ['emp_name','emp_id','emp_email']

admin.site.register(Employee,Employee_admin)