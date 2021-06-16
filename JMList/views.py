from django.shortcuts import render, redirect
from django.http import HttpResponse
from JMList.models import Employee, ValidID, Department, EmployeesHealth, WorkHistory

#list 1st model
#items 2nd model

def homepage(request):
	employees = Employee.objects.all()
	return render(request, 'homepage.html',{'employees' : employees})

def view_list(request, employee_id):
	#validid_ = ValidID.objects.get(id=employee_id)
	return render(request, 'idlist.html', {'employee_':employee_})

def new_list(request):
	#employee_ = Employee.objects.create()
	#ValidID.objects.create(Name=request.POST['newEmployee'], Address=request.POST['newAddress'],employee=employee_)
	return redirect(f'/JMList/{employee_.id}/')

def add_item(request, employee_id):
	#employee_ = Employee.objects.get(id=employee_id)
	#ValidID.objects.create(ValID=request.POST['validEntry'],ValNum=request.POST['validNumber'],employee=employee_)
	return redirect(f'/JMList/{employee_.id}/')
'''
def dataManipulation(request):
	#Creating
	employee = Employee(Name="", Address ="", PhoneNumber="", EmailAddress="")
	employee = Employee(Name="Jhoanna Marie Lopez", Address ="B5 L14 Bonifacio St., Windsor Homes Subd., Brgy. Burol III, Dasmarinas City, Cavite", PhoneNumber="09478766415", EmailAddress="jhoannamarie.lopez@gsfe.tupcavite.edu,ph")
	employee.save()

	#Read all in employee
	objects = Employee.objects.all()
	employee = Employee.objects.all()
	result ='Printing all of the entries under Employee model : <br>'
	for x in objects:
		result += x.Name+"<br>"

	#Read specific entry in employee
	ename = Employee.objects.get(id="")
	result += 'Printing only one entry <br>'
	result += ename.PhoneNumber
	employeename = Employee.objects.get(id="employee")
	res += 'Printing only one entry <br>'
	res += employeename.Name

	#Delete
	result += 'Deleting an entry <br>'
	ename.delete()
	res += 'Deleting an entry <br>'
	employeename.delete()

	#Update
	employee = Employee.objects.get(name ='')
	employee.PhoneNumber = ""
	employee = Employee.objects.get(name ='Jhoanna Marie Lopez')
	employee.PhoneNumber = "09614423655"
	employee.save = ""
	res = ""

	#Filtering
	jm = ValidID.objects.filtered(Name = "")
	result += "Found : %s results <br>" % len (jm)
	qs = Employee.objects.filtered(Name = "Jhoanna Marie Lopez")
	res += "Found : %s results <br>" % len (qs)

	#Ordering
	jm = Employee.objects.ordered_by("Address")
	for x in jm:
	qs = Employee.objects.ordered_by("Address")
	for x in qs:
		result += x.Name + x.Address + '<br>'
'''


'''
def homepage(request):
	items = Item.objects.all()
	return render(request, 'homepage.html',{'items' : items})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'idlist.html', {'list':list_})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['newFirst'],last=request.POST['newLast'],list=list_)
	return redirect(f'/JMList/{list_.id}/')

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(valID=request.POST['validEntry'],valNum=request.POST['validNumber'],date=request.POST['validDate'],list=list_)
	return redirect(f'/JMList/{list_.id}/')
	'''
