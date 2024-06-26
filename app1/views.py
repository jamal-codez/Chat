from ast import If
from django.views.generic import View
from contextvars import Context
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from app1.forms import Acct, Update, Userf
from .forms import *
from .models import *
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    tem=loader.get_template('home.html')
    #m=Chat.objects.get(id=id)
    #cont={
      #  'm':m
    #}
    return HttpResponse(tem.render({},request))

def personal_info(request):
    t=loader.get_template('personal_info.html')
    return HttpResponse(t.render({},request))

def update(request, id):
    t=loader.get_template('update.html')
    z=Chat.objects.get(id=id)
    #y={
     #   'cat':z.user,
      #  'fname':'fghjk',
       # 'lname':z.lname,
        #'passw':z.passw,
        #'ph':z.ph,
        #'birth':z.birth,
        #'mail':z.mail,
        #'country':z.country,
        #'adrs':z.adrs,
        #'mg':z.mg
    #}
    form=Update(request.POST, request.FILES, initial={'user':'jamalll'})
    cont={
        'form':form,
        'm':z
    }
    return HttpResponse(t.render(cont,request,))

def updaterecord(request, id):
    z=Chat.objects.get(id=id)
    form=Update(request.POST, request.FILES, instance=z)
    if form.is_valid:
        form.save()
        return HttpResponseRedirect(reverse('personal_info', args=(z.id,)))
    else:
        error="Enter Valid data"
        return HttpResponseRedirect(reverse('update ', args=(z.id,)))

def datab(request):
    users=Chat.objects.all().values
    tem=loader.get_template('data.html')
    cont={
        'users':users
    }
    return HttpResponse(tem.render(cont,request))
def index(request):
    tem=loader.get_template('index.html')
    return HttpResponse(tem.render())


def acct(request):
    tem=loader.get_template('add.html')
    form1=Userf(request.POST)
    form2=Acct(request.POST, request.FILES)
    return HttpResponse(tem.render({'form1':form1,'form2':form2},request))
    

def acctrecord(request):
    form1=Userf(request.POST)
    form2=Acct(request.POST, request.FILES)
    if form2.is_valid() and form1.is_valid():
        u=form1.save()
        ac=form2.save(commit=False)
        ac.user=u
        ac.save()
        messages.success(request,  'Your account has been successfully created')
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('acct'))


class CreateThread(View):
  def get(self, request, *args, **kwargs):
    form = ThreadForm()
    context = {
      'form': form
    }
    return render(request, 'create_model.html', context)
  def post(self, request, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    try:
      receiver = User.objects.get(username=username)
      if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('thread', pk=thread.pk)
      
      if form.is_valid():
        sender_thread = ThreadModel(
          user=request.user,
          receiver=receiver
        )
        sender_thread.save()
        thread_pk = sender_thread.pk
        return redirect('thread', pk=thread_pk)
    except:
      return redirect('create-thread')

class ListThreads(View):
  def get(self, request, *args, **kwargs):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    context = {
        'threads': threads 
    }
    return render(request, 'inbox.html', context)

class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    thread = ThreadModel.objects.get(pk=pk)
    #message=MessageForm(request.POST, request.FILES)
    if thread.receiver == request.user:
        
        receiver = thread.user
        #if message.is_valid():
            #message.receiver_user=thread.user
            #message.sender_user=request.user
            #message.save()
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST['message'],
            image=request.FILES.get('attach_image'),
            file=request.FILES.get('attach_file'),
        )
        message.save()
    else:
        #if message.is_valid():
            #message.receiver_user=thread.receiver
            #message.sender_user=request.user
            #message.save()
        receiver = thread.receiver
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST['message'],
            image=request.FILES.get('attach_image'),
            file=request.FILES.get('attach_file'),
        )
        message.save()
    return redirect('thread', pk=pk)

class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm(request.POST)
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list,
    }
    return render(request, 'thread.html', context)