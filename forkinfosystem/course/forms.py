from django import forms
from django.forms import ModelForm
from .models import Contact_Us
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact_Us
		fields = '__all__'



		
		
