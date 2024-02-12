from django import forms
from .models import Donor_Detail

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Donor_Detail
		fields=('first_name','last_name','email','mobile','age','area','state','city','gender')
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'last_name':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'email':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'mobile':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'age':forms.NumberInput(attrs={'class':'form-control py-1 ps-3'}),
		'area':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'city':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'state':forms.TextInput(attrs={'class':'form-control py-1 ps-3'}),
		'gender':forms.RadioSelect()
		}

