from django.urls import path
from . import views

app_name= 'home'
urlpatterns = [
    path ('', views.home , name='home'),
    path ('con/', views.contact_us , name='contact'),
    path ('getmessage/', views.getmessage , name='getmessage'),
    path ('about/', views.getmessage , name='about'),

]
