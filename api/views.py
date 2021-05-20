from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'list.html', context)


def employee_form(request, id=0):
    # Get the data or form from database
    if request.method == "GET":
        # Its Insert operation (ex:add new in list template)
        if id == 0:
            form = EmployeeForm()
        #EDit operation    
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "form.html", {'form': form})
       
    else:
        # retrieve the data and send the data to database
        if id == 0:
            form = EmployeeForm(request.POST)
        # Updated data send to database    
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/')
