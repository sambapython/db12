from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reg(request):
	
	#temp=30
	return render(request,"students/home.html")
	#return HttpResponse("<h1>user registration</h1>")
def inst(request):
	return HttpResponse("adfas")
