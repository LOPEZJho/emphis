from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
	return HttpResponse('<html><title>Student List</title></html>')
# Create your views here.
