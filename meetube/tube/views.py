from django.shortcuts import render, redirect
from tube.models import Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def logout_view(request):
	logout(request)
	return redirect("/")
def login_view(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		user = authenticate(username=data.get("username"),
			password=data.get("password"))
		if user:
			# request.session.
			login(request,user)
			# add the user details to session
			# request.user.is_authenticated
			msg="login success "
		else:
			msg="login failed"

	return render(request, "tube/login.html",{"msg":msg})
def register_view(request):
	msg=""
	if request.method == "POST":
		data=request.POST
		user = User.objects.create_user(data.get("username"),
			data.get("password"))
		user.email=data.get("email")
		user.save()
		msg="Registed successfully"

	return render(request,"tube/register.html",{"msg":msg})
def index_view(request):
	public_videos = Video.objects.filter(type="public")
	return render(request,"tube/index.html",{"videos":public_videos})
