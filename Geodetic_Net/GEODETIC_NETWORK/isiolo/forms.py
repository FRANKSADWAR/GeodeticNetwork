from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from isiolo.models import StaffProfiles, ReportIncidence
from django.contrib.gis import forms as gis_forms
import logging
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget, GoogleStaticOverlayMapWidget


logger = logging.getLogger(__name__)

## Report control station incidence 
class ReportIncidenceForm(gis_forms.ModelForm):
    class Meta:
        model = ReportIncidence
        fields = ('station_name','status','username','organization','phone_no','email','coordinates')

        widgets = {
            'coordinates':GooglePointFieldWidget
        }


## LOGIN FORM FOR THE USER IN THE SITE
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

## REGISTER AS A NEW USER TO THE SYSTEM
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    pssword2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def passlen(self):
        passdata = self.cleaned_data['password']
        if passdata.__len__() < 8:
            raise ValidationError('Password is very short')
        return passdata

    def clean_password2(self):
        cd = self.cleaned_data['password2']  
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords dont\'t match ')  
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if "@" not in cd['email']:
            raise ValidationError('Enter a valid email address')
        return cd['email']    

## USERS IN THE SYSTEM CAN EDIT THEIR DETAILS
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = StaffProfiles
        fields = ('user','telnumber','address','photo')        


