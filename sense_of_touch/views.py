from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def index(request):
    return render(request,"sense_of_touch/Home.html")

def contact(request):
    if request.method == "POST":
        message_name = request.POST['name'] 
        message_email = request.POST['email'] 
        message = request.POST['message'] 

        send_mail(message_name,  message, settings.EMAIL_HOST_USER,
        [''], fail_silently=False)

        return render(request,"sense_of_touch/contact.html",{
            'message_name':message_name,
            "message": "Thanks!  We received your email and will respond soon..."
            
        })
    else:
        return render(request,"sense_of_touch/contact.html")

def gallery(request):
    return render(request,"sense_of_touch/Gallery.html")

def about(request):
    return render(request,"sense_of_touch/About.html")

