from django.shortcuts import render, redirect
from tube.models import Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from tube.forms import VideoSearchForm, VideoCreateForm
from django.views.generic import CreateView
from django.db.models import Q

def get_videos(request):
	if request.user.is_authenticated:
		videos = Video.objects.filter(
			Q(user=request.user) | Q(type="public") | Q(type="semi-public")
			)
	else:
		videos = Video.objects.filter(type="public")
	params = request.GET 
	if params:
		category = params.get("category")
		name=params.get("name")
		tags = params.get("tags")
		if category:
			videos = videos.filter(category__name__iexact=category)
		if name:
			videos = videos.filter(name__iexact=name)
		if tags:
			videos = videos.filter(tags__in=tags)

	return videos


# Create your views here.
def videolist(request):
	videos = get_videos(request)
	return render(request,"tube/video_list.html",
		{"videos":videos})

def uploadview(request):
	if request.method=="POST":
		data = request.POST
		form = VideoCreateForm(data =data, files=request.FILES)
		if form.is_valid():
			form.save()
			video = form.instance
			video.user = request.user
			video.save()
			return redirect("/videos/")
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
	try:
		if request.method == "POST":
			data=request.POST
			user = User.objects.create_user(data.get("username"),
				data.get("email"),
				data.get("password"))
			msg="Registed successfully"
	except Exception as err:
		msg=err
	return render(request,"tube/register.html",{"msg":msg})
def index_view(request):
	videos = get_videos(request)
	form = VideoSearchForm(data=request.GET)
	return render(request,"tube/index.html",{"videos":videos,
		"form":form})
