from django.shortcuts import render, redirect
from django.http import HttpResponse
from JMList.models import Item, List

#list 1st model
#items 2nd model

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
def dataManipulation(request):
	#Creating
	employee = Employee(Name="Jhoanna Marie Lopez", Address ="B5 L14 Bonifacio St., Windsor Homes Subd., Brgy. Burol III, Dasmarinas City, Cavite", PhoneNumber="09478766415", EmailAddress="jhoannamarie.lopez@gsfe.tupcavite.edu,ph")
	employee.save()

	#Read all in employee
	employee = Employee.objects.all()
	result ='Printing all of the entries under Employee model : <br>'
	for x in objects:
		result += x.Name+"<br>"

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
'''





'''	
	if request.method == 'POST':
		Item.objects.create(text=request.POST['validEntry'])
		return redirect('/')
	items = Item.objects.all()
	return render(request,'homepage.html',{'items':items})'''


#def homepage(request):
	#return render(request,'homepage.html',{'validEntry':request.POST.get('validEntry',''),'validNumber':request.POST.get('validNumber',''),'validDate':request.POST.get('validDate',''),})

'''def homepage(request):
	item1 = Item()
	item1.text=request.POST.get('validEntry','')
	item1.save()
	return render(request,'homepage.html',{'newEntry': item1.text,})

#def homepage(request):
	if request.method == 'POST':
		newItem = request.POST['validEntry']
		Item.objects.create(text=newItem)
	else:
		newItem=''
	return render(request,'homepage.html',{'newEntry':newItem,})'''


#from django.shortcuts import render
#from django.http import HttpResponse
																																																																																																																																																																																																				
#def home_page(request):																																																													
#	return HttpResponse('<html><title>Student List</title></html>')																																		
# Create your views here