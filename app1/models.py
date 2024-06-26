


from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from time import timezone
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Chat(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    ph=models.BigIntegerField( blank=False)
    birth=models.DateField( blank=False)
    country=models.CharField(max_length=100,  blank=False)
    adrs=models.CharField(max_length=100,  blank=True)
    mg = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.user.username)

class ThreadModel(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver= models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    has_read= models.BooleanField(default=False)

class MessageModel(models.Model):
    thread=models.ForeignKey(ThreadModel,on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    sender_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body=models.TextField()
    image=models.ImageField(upload_to='images/', blank=True,null=True )
    file=models.FileField(upload_to='files/',blank=True,null=True)
    date=models.DateField(default= datetime.now )
    is_read= models.BooleanField(default=False)