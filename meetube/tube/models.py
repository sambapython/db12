from django.db import models

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=250)

class Video(models.Model):
	type_choices = [('public','public'),('semi-public','semi-public'),
	("private","private")]
	name = models.CharField(max_length=250, blank=True, null=True)
	link = models.FileField()
	description = models.TextField(max_length=250,blank=True, null=True)
	type = models.CharField(choices=type_choices,default="public", max_length=250)
	tags = models.CharField(max_length=250)
	#comments
	#watchers
	#rating
	#views
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	uploadate = models.DateTimeField(auto_now_add=True)

