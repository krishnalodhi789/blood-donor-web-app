from django.db import models





 
class Donor_Detail(models.Model):
	first_name=models.CharField(max_length=32)
	last_name=models.CharField(max_length=32)
	email=models.EmailField()
	mobile=models.CharField(max_length=23)
	gender=models.CharField(max_length=32,choices=(('Male','Male'),('Female','Female')))
	age=models.IntegerField(help_text='Age must be greater then 18. and less then 45',)
	state = models.CharField(max_length=32)
	city = models.CharField(max_length=32)
	area = models.CharField(max_length=32)
	available = models.BooleanField(default=True)
	blood_group =models.CharField(max_length=5)


# For Go back to registration form ,fill th values
class Temp_data(models.Model):
	first_name=models.CharField(max_length=32)
	last_name=models.CharField(max_length=32)
	email=models.EmailField()
	mobile=models.CharField(max_length=10)
	gender=models.CharField(max_length=32,choices=(('Male','Male'),('Female','Female')))
	age=models.IntegerField(help_text='Age must be greater then 18.',)
	state = models.CharField(max_length=32)
	city = models.CharField(max_length=32)
	area = models.CharField(max_length=32)
	availabe = models.BooleanField(default=True)
	otp = models.CharField(max_length=6)

