from django.shortcuts import render,redirect
from django import forms  
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.template.context_processors import csrf
from django.contrib.auth import authenticate,login 
from .models import customer
from .forms import MyRegistrationForm,loginForm

def register_user(request):
	form = MyRegistrationForm(request.POST or None)
	context = {
	    "form": form
	}
	if form.is_valid():
		form.save()
		context['form'] = MyRegistrationForm()
	return render(request,"register.html",context)

def login_user(request):
	form = loginForm(request.POST or None)
	context = {
	    "form": form
	}
	if form.is_valid():
		password = form.cleaned_data.get("password")
		username = form.cleaned_data.get("username")
		userlist = customer.object.all().values('username')
		user     = authenticate(request,username=username,password=password)
		userlist1= customer.object.filter(username = username).exists()
		userlist2= customer.object.filter(password = password).exists()
		print(userlist2)
		if userlist1 and userlist2:
			login(request,user)
			return redirect("/home")
		else:
			print('error23')
	return render(request,"login.html",context)

def home_page(request):
	return render(request,"index.html",{})