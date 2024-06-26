from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', views.index, name='index1'),
    path('acct/',views.acct, name='acct'),
    path('acct/acctrecord/', views.acctrecord, name='acctrecord'),
    path('datab/', views.datab, name='datab'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', views.loginpg, name='login'),
    #path('login/loginauth/', views.loginauth, name='loginauth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/',views.home,name='home'),
    path('personal_info/',views.personal_info,name='personal_info'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message')
    
]