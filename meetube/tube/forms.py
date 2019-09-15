from django.forms import ModelForm
from tube.models import Video

class VideoSearchForm(ModelForm):
	class Meta:
		model = Video
		fields = ['name',"tags","category"]
class VideoCreateForm(ModelForm):
	class Meta:
		model = Video
		exclude = ["user"]