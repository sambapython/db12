from django.forms import ModelForm
from tube.models import Video
from django import forms

class VideoSearchForm(forms.Form):
	name=forms.CharField(max_length=250,required=False)
	tags=forms.CharField(max_length=250, required=False)
	category = forms.CharField(max_length=250, required=False)
class VideoCreateForm(ModelForm):
	class Meta:
		model = Video
		exclude = ["user"]