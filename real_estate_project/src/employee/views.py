from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
from django.contrib import messages

# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST,request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your property add successfully!! thank you :)')
            return redirect('/addproperty')  
    else:
    	form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
