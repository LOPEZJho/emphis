from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request,'homepage.html',{'validEntry':request.POST.get('validEntry',''),'validNumber':request.POST.get('validNumber',''),'validDate':request.POST.get('validDate',''),})

#from django.shortcuts import render
#from django.http import HttpResponse
																																																																																																																																																																																																				
#def home_page(request):																																																													
#	return HttpResponse('<html><title>Student List</title></html>')																																		
# Create your views here