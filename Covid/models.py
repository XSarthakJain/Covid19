from django.db import models

# Create your models here.
class Covid(models.Model):
	pic=models.ImageField(upload_to="profiles")
	Full_Name=models.CharField(max_length=50,default="")
	Age=models.CharField(max_length=20,default="")
	Gender=models.CharField(max_length=20,default="")
	Fever=models.CharField(max_length=25,default="")
	BodyPain=models.CharField(max_length=20,default="")
	Email=models.CharField(max_length=25,default="")
	RunnyNose=models.CharField(max_length=20,default="")
	Cough=models.CharField(max_length=20,default="")
	Breath=models.CharField(max_length=20,default="")
	InfectionProb=models.CharField(max_length=20,default="")
	OTP=models.CharField(max_length=20,default="")
	

class Patients(models.Model):
	latitude=models.CharField(max_length=50,default="")
	longitude=models.CharField(max_length=50,default="")
	city=models.CharField(max_length=50,default="")

