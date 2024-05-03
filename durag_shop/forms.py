from django import forms
from .models import branch,manager,doctor,employer,patient,CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class loginform(AuthenticationForm):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    


class customUsercretionForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','is_doctor','is_manager','is_employer','is_patient']



class managerceationForm(forms.ModelForm):
    class Meta:
        model=manager
        fields=['user','name','branch']

    
    

class docterceationForm(forms.ModelForm):
    class Meta:
        model=doctor
        fields=['user','name','branch']
   
class employerceationForm(forms.ModelForm):
    class Meta:
        model=employer
        fields=['user','name','branch']
   
class patientceationForm(forms.ModelForm):
    class Meta:
        model=patient
        fields=['user','name','branch']
   
class branchrceationForm(forms.ModelForm):
    class Meta:
        model=branch
        fields=['name','location']
   
