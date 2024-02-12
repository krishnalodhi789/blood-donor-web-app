from django.contrib import admin
from .models import Donor_Detail,Temp_data

@admin.register(Donor_Detail)
class Condidate_Fields(admin.ModelAdmin):
	list_display=('id','first_name','last_name','email')


@admin.register(Temp_data)
class Temp_Fields(admin.ModelAdmin):
	list_display=('id','first_name','last_name','email','age','state','city','area',)