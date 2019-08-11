from django.shortcuts import render
import psutil
from django.http import HttpResponse
from management.models import UserProfile
from django.contrib.auth import authenticate
from management.forms import CourseForm
# Create your views here.
def create_course_view(request):
	cf = CourseForm()
	return render(request,"management/course_form.html",
		{"form":cf})
def courses_offered_view(request):
	return render(request,"management/course_list.html")
def get_cores(request):
	number_cores = psutil.cpu_count()
	return HttpResponse(number_cores)
def manage(request):
	return render(request,"management/home.html")
def home_view(request):
	if request.method == "GET":
		msg=""
		
	else:
		data = request.POST
		if "reg" in data:
			user  =UserProfile(
				username=data.get('username'),
				password=data.get('password'), 
				email = data.get('email'),
				phone=data.get("phone"))
			user.save()
			user.set_password(data.get('password'))
			user.save()
			msg = "registered successfully"
		if "log" in data:
			user = authenticate(username=data.get("username"),
				password=data.get("password"))
			if user:
				msg="login successfully"
			else:
				msg="Login failed.."
	return render(request,"management/home.html",{"message":msg})
