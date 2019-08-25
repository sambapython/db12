"""meetube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView, ListView, CreateView,\
UpdateView, DeleteView
from tube.models import Category

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="tube/index.html")),
    path("categories/", ListView.as_view(model = Category)),
    path("create_category/", CreateView.as_view(
    	model=Category,
    	success_url="/categories",
    	fields="__all__",
    	) ),
    re_path("update_category/(?P<pk>[0-9]+)",UpdateView.as_view(model=Category,
    	success_url="/categories",
    	fields= ["name"] #"__all__",
    	)),
    re_path("delete_category/(?P<pk>[0-9]+)",DeleteView.as_view(model=Category,
        success_url="/categories")),
]
