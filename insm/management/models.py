from django.db import models
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
	roles  =[('student',"student"),("boardmember","boardmember"),("instructor","instructor")]
	phone = models.IntegerField(blank=True, null=True)
	role = models.CharField(choices = roles, default="student",max_length=20)

class abs(models.Model):
	# abstract model, This model dont have table in the database.
	name = models.CharField(max_length=250) 
	status = models.BooleanField(default=True)
	class Meta:
		abstract=True

# Create your models here.
class BoardMember(abs):
	# DateTimeField, DateField, BooleanField, IntegerField, FileField, ImageField
	
	role = models.CharField(max_length=256)
	phone = models.IntegerField()
	email = models.CharField(max_length=250)
	pic = models.ImageField(blank=True, null=True)
class Student(abs):
	phone = models.IntegerField()
	email = models.CharField(max_length=250)
	pic = models.ImageField(blank=True, null=True)
class Instructor(abs):
	#id_p = models.CharField(primary_key=True)
	expertise = models.CharField(max_length=500)
	phone = models.IntegerField()
	email = models.CharField(max_length=250)
	pic = models.ImageField(blank=True, null=True)


class Course(abs):
	startdate = models.DateTimeField()
	enddate = models.DateTimeField()
	instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT)
	fee = models.IntegerField()



	



