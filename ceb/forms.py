from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'last_name', 'last_name', 'email', 'password1', 'password2']