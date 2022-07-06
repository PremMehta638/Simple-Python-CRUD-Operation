from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required


def list_employee(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)

@login_required(login_url='login')
def register_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST,files= request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'employee_register/employee_form.html', {'form': form})

@login_required(login_url='login')
def update_employee(request, pk):
    employee =Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'employee_register/employee_form.html', {'form': form})

@login_required(login_url='login')
def delete_employee(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('list')
