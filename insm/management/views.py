from django.shortcuts import render
import psutil
from django.http import HttpResponse
# Create your views here.
def get_cores(request):
	number_cores = psutil.cpu_count()
	return HttpResponse(number_cores)
def manage(request):
	return render(request,"management/home.html")
