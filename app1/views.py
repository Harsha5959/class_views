from django.shortcuts import render,redirect
from app1.models import Employee
from django.views import View
from app1.form import Employee_Form

'get'

class get_employees(View):
    def get(self,request):
        data = Employee.objects.all()
        context = {
            'data':data
        }
        return render(request,'home.html',context)
    
'create'

class new_employee(View):
    def get(self,request):
        form = Employee_Form()
        return render(request,'emp_form.html',{'form':form})
    def post(self,request):
        form = Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            form = Employee_Form()
        context ={
            'form':form
        }

        return render(request,'emp_form.html',context)

class emp_delete(View):
    def get(self,request,id):
        data = Employee.objects.get(id=id)
        data.delete()
        return redirect('homepage')
    
class emp_update(View):
    def get(self,request,id):
        data = Employee.objects.get(id=id)
        form = Employee_Form(instance=data)
        return render(request,'emp_form.html',{'form':form})
    def post(self,request,id):
        data = Employee.objects.get(id=id)
        form = Employee_Form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            form = Employee_Form(instance=data)
            context = {
                'form':form
            }
            return render(request,'emp_form.html',context)
        