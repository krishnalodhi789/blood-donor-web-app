from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registration/',views.registration,name='registration'),
    path('otpVerify/',views.otpVerify,name='otpVerify'),
    path('chooseBloodGroup/',views.chooseBloodGroup,name='chooseBloodGroup'),
    path('profile/',views.profile,name='profile'),
]
