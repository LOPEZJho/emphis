from django.shortcuts import render, redirect
from django.http import HttpResponse
from JMList.models import Item

def homepage(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['newFirst'])
		return redirect('/')
	return render(request,'homepage.html')


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