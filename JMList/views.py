from django.shortcuts import render, redirect
from django.http import HttpResponse
from JMList.models import Employee, ValidID

#list 1st model
#items 2nd model

def homepage(request):
	employees = Employee.objects.all()
	return render(request, 'homepage.html',{'employees' : employees})

def view_list(request, employee_id):
	validid_ = ValidID.objects.get(id=employee_id)
	return render(request, 'idlist.html', {'employee':employee_})

def new_list(request):
	EmpID_ = Employee.objects.create()
	Employee.objects.create(Name=request.POST['newEmployee'],Address=request.POST['newAddress'],employees=EmpID_)
	return redirect(f'/JMList/{employee_.id}/')

def add_item(request, employee_id):
	EmpID_ = Employee.objects.get(id=employee_id)
	ValidID.objects.create(ValID=request.POST['validEntry'],ValNum=request.POST['validNumber'],employees=EmpID_)
	return redirect(f'/JMList/{employee_.id}/')


def dataManipulation(request):
	#Creating
	employee = Employee(Name="Jhoanna Marie Lopez", Address ="Windsor Homes Subd., Brgy. Burol III, Dasmarinas City, Cavite", PhoneNumber="09478766415", EmailAddress="jhoannamarie.lopez@gsfe.tupcavite.edu,ph")
	employee.save()

	#Read all in employee
	employee = Employee.objects.all()
	result ='Printing all of the entries under Employee model : <br>'
	for x in objects:
		result == x.Name+"<br>"

	#Read specific entry in employee
	employeename = Employee.objects.get(id="employee")
	res += 'Printing only one entry <br>'
	res += employeename.Name

	#Delete
	res += 'Deleting an entry <br>'
	employeename.delete()

	#Update
	employee = Employee.objects.get(name ='Jhoanna Marie Lopez')
	employee.PhoneNumber = "09614423655"
	employee.save = ""
	res = ""

	#Filtering
	qs = Employee.objects.filtered(Name = "Jhoanna Marie Lopez")
	res += "Found : %s results <br>" % len (qs)

	#Ordering
	qs = Employee.objects.ordered_by("Address")
	for x in qs:
		result += x.Name + x.Address + '<br>'