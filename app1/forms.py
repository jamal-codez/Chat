
from dataclasses import field
from django.core.exceptions import ValidationError
from pyexpat import model
from django.forms import ModelForm, widgets
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Acct(forms.ModelForm):
    ch=(
        (None,"Choose"),
        ("Nigeria","Nigeria"),
        ("Mozambique","Mozambique"),
        ("Tanzania","Tanzania"),
        ("Uganda","Uganda"),
        ("Angola","Angola"),
        ("sudan","sudan"),
    )
    ph=forms.IntegerField(label='Phone Number',widget=forms.NumberInput(attrs={'required':'True'}),required=False )
    birth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date of Birth',required=False)
    country=forms.ChoiceField(widget=forms.Select(attrs={'required':'True'}), choices=ch,required=False)
    adrs=forms.CharField(label='Address',required=False,widget=forms.TextInput(attrs={'placeholder':'Kharthoum, Sudan'}))
    mg= forms.ImageField(label='Upload Image',required=False, widget=forms.FileInput(attrs={'required':'True'}))
    class Meta:
        model=Chat
        fields=['ph','birth','country','adrs','mg']
        

class Userf(UserCreationForm):
    #password1= forms.CharField(label='Password', required= False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'required':'True'}))
    #password2= forms.CharField(label='Re-Enter Password', required= False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'required':'True'}))
    class Meta:
        model=User
        fields= ['username','first_name','last_name','password1','password2','email']
        
class Update(forms.ModelForm):
    ch=(
        (None,"Choose"),
        ("Nigeria","Nigeria"),
        ("Mozambique","Mozambique"),
        ("Tanzania","Tanzania"),
        ("Uganda","Uganda"),
        ("Angola","Angola"),
        ("sudan","sudan"),
    )
    mg= forms.ImageField(label='Change Profile Image',required=False, widget=forms.FileInput(attrs={'required':'True'}))
    user=forms.CharField(max_length=200, label='Username', required=False, widget=forms.TextInput(attrs={'required':'True'}))
    fname=forms.CharField(max_length=200, label='First Name',required=False, widget=forms.TextInput(attrs={'required':'True'}))
    lname=forms.CharField(max_length=200, label='Last Name',required=False,widget=forms.TextInput(attrs={'required':'True'}))
    passw=forms.CharField(max_length=10,label='Password',required=False, widget=forms.PasswordInput(attrs={'required':'True'}))
    ph=forms.IntegerField(label='Phone Number',widget=forms.NumberInput(attrs={'required':'True'}),required=False )
    birth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date of Birth',required=False)
    mail=forms.EmailField(widget=forms.EmailInput(attrs={'required':'True'}),label='Email Address',required=False)
    country=forms.ChoiceField(widget=forms.Select(attrs={'required':'True'}), choices=ch,required=False)
    adrs=forms.CharField(label='Address',required=False,widget=forms.TextInput(attrs={'placeholder':'COUNTRY'}))
    
    class Meta:
        model=Chat
        fields=['user','fname','lname','passw','ph','birth','mail','country','adrs','mg']

class ThreadForm(forms.Form):
    username=forms.CharField(max_length=100)
class  MessageForm(forms.Form):
    #body=forms.CharField(label='message',max_length=1000,required=False, widget=forms.TextInput(attrs={'type':'text', 'required':'True','placeholder':'Write you message here'}))
    #image= forms.ImageField(label='attach_image',required=False)#, widget=forms.FileInput(attrs={'required':'False'}))
    #file= forms.FileField(label='attach_file',required=False)#, widget=forms.FileInput(attrs={'required':'False'}))
    message=forms.CharField(max_length=1000,required=False)
    attach_image= forms.ImageField(required=False)#, widget=forms.FileInput(attrs={'required':'False'}))
    attach_file= forms.FileField(required=False)#, widget=forms.FileInput(attrs={'required':'False'}))
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        if 'message' in self.data:
            message=self.data.get('message')
            a_img=self.data.get('attach_image')
            a_file=self.data.get('attach_file')
            if a_img or a_file:
                self.fields['message'].widget=forms.TextInput(attrs={'type':'text','required':'False','placeholder':'Write you message here'})
            else:
                self.fields['message'].widget=forms.TextInput(attrs={'type':'text','required':'True','placeholder':'Write you message here'})
    #class Meta:
        #model= MessageModel**********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
        #fields=['body','image','file']****