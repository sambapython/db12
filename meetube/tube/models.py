from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=250)

	def __str__(self):
		"""
		while you are printing the Category object in the front end, this method
		will be called and show the only name column value(As per definition.)
		"""
		return self.name

class Video(models.Model):
	type_choices = [('public','public'),('semi-public','semi-public'),
	("private","private")]
	name = models.CharField(max_length=250, blank=True, null=True)
	link = models.FileField()
	description = models.TextField(max_length=250,blank=True, null=True)
	type = models.CharField(choices=type_choices,default="public", max_length=250)
	tags = models.CharField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
	#comments
	#watchers
	#rating
	#views
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	uploadate = models.DateTimeField(auto_now_add=True)

