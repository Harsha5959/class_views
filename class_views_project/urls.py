"""
URL configuration for class_views_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import get_employees,new_employee,emp_delete,emp_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_employees.as_view(),name='homepage'),
    path('add_emp',new_employee.as_view(),name='add_emp'),
    path('del_emp<int:id>',emp_delete.as_view(),name='del_emp'),
    path('update_emp<int:id>',emp_update.as_view(),name='update_emp'),
]
