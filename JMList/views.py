from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')



#from django.shortcuts import render
#from django.http import HttpResponse

#def home_page(request):
#	return HttpResponse('<html><title>Student List</title></html>')
# Create your views here.
