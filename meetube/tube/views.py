from django.shortcuts import render, redirect
from tube.models import Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from tube.forms import VideoSearchForm, VideoCreateForm
from django.views.generic import CreateView

# Create your views here.
def uploadview(request):
	if request.method=="POST":
		data = request.POST,
		data["user"] = request.user.id
		form = VideoCreateForm(data =data, files=request.FILES)
		if form.is_valid():
			form.save()
		else:
			msg= form._errors
			return render(request,"tube/video_form.html",{"form":form,"msg":msg})
	else:
		form = VideoCreateForm()
		return render(request,"tube/video_form.html",{"form":form})

	

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
	form = VideoSearchForm()
	return render(request,"tube/index.html",{"videos":public_videos,
		"form":form})
