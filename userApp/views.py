from django.shortcuts import render,redirect
from . forms import RegistrationForm
from . models import Temp_data
import random 

def home(req):
	return render(req,'index.html')

def chooseBloodGroup(req):
	if req.method == 'POST':
		temp=Temp_data.objects.all()
		otp = temp[0].otp
		mobile=temp[0].mobile		
		userOtp = req.POST.get('otp')
		if otp == userOtp:
			return render(req,'chooseBloodGroupForm.html')
		else:
			return render(req,'otpVerify.html',{'invalid':True,'mobile':mobile})
			
	return render(req,'chooseBloodGroupForm.html')



def profile(req):
	if(req.GET):
		bg=req.GET.get('BloodGroup')
		print(bg)
		return redirect('home')
	else:
		return render(req,'chooseBloodGroupForm.html',)





    

def registration(req):
	try:
		data=Temp_data.objects.all()
		fname = data[0].first_name
		lname = data[0].last_name
		email = data[0].email
		mobile= data[0].mobile
		gender= data[0].gender
		age= data[0].age
		state= data[0].state
		city= data[0].city
		area= data[0].area

		data.delete()

		form=RegistrationForm(initial={
			'last_name':lname,
			'first_name':fname,
			'email':email,
			'mobile':mobile,
			'gender':gender,
			'state':state,
			'city':city,
			'area':area,
			'age':age,
			})
	except Exception as e:
		form=RegistrationForm()


	return render(req,'registration.html',{'form':form})

def otpVerify(req):
	temp = Temp_data.objects.all().delete()
	try:
		if req.method == 'POST':
			otp = random.randint(100000,999999)
			form =RegistrationForm(req.POST)
			if form.is_valid():
				fname=form.cleaned_data.get('first_name')
				lname=form.cleaned_data.get('last_name')
				email=form.cleaned_data.get('email')
				mobile=form.cleaned_data.get('mobile')
				gender=form.cleaned_data.get('gender')
				state=form.cleaned_data.get('state')
				city=form.cleaned_data.get('city')
				area=form.cleaned_data.get('area')
				age=form.cleaned_data.get('age')
				
				temp = Temp_data(
					first_name=fname,
					last_name=lname,
					email=email,
					mobile=mobile,
					gender=gender,
					state=state,
					city=city,
					area=area,
					age=age,
					otp=otp 
					)
				temp.save()
				responce = render(req, 'otpVerify.html',{'mobile':mobile})
				responce.set_cookie('userId',temp.id)
				return responce
	except Exception as e:
		return render(req,'registration.html',{'form':form,'feil':True})
		