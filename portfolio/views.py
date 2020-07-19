from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactUS
from .models import messagedata

# Create your views here.

def home (request):
    pro = Project.objects.all()
    return render (request, 'portfolio/home.html', {'pro': pro})

def contact_us (request):
    context ={
        "form": ContactUS
    }
    return render(request, 'portfolio/contact_us.html',context)

def getmessage (request):
    form = ContactUS(request.POST)

    if form.is_valid():
        myregister =messagedata(full_name =form.cleaned_data['full_name'],
        email =form.cleaned_data['email'],
        phone =form.cleaned_data['phone'],
        message =form.cleaned_data['message'],)

        myregister.save()

    return redirect('home:home')

def about_us (request):
    return render(request, 'portfolio/about.html')
