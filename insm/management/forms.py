from django.forms import ModelForm
from management.models import Course

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = "__all__"