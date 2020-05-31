from django.contrib.auth.models import User
from django import forms
from .models import StudentData

# Create your tests here.

class UserRegisterForm(forms.ModelForm):
 

    class Meta:
        model = StudentData
        fields = '__all__'

