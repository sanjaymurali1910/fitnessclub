import os
import random
from django.shortcuts import render, redirect
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import *
# Create your views here.



def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about-us.html')

def classes(request):
	return render(request, 'classes.html')

def train(request):
	return render(request, 'Trainer.html')

def selecttrainer(request):
	return render(request, 'selecttrainer.html')

def startnow(request):
	return render(request, 'startnow.html')

def shedule(request):
	return render(request, 'timetable.html')

def contact(request):
	return render(request, 'contact.html')   

def signup(request):
	return render(request, 'signup.html')

def join(request):
	return render(request, 'join.html')

def userpayment(request):
	return render(request, 'user_payment.html')

def userpaymentpage(request):
	return render(request, 'user_pay_page.html')

def login(request):
	return render(request, 'login.html')

def online_training(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		e=request.POST['email']

		onlinetraining.objects.create(firstname=fn,lastname=ln,email=e)
        

	return render(request, 'online_training.html')

def offline_training(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		e=request.POST['email']

		offlinetraining.objects.create(firstname=fn,lastname=ln,email=e) 

	return render(request, 'offline_training.html')




def traindex(request):
	return render(request, 'traind.html')

def onlin(request):
	online=onlinetraining.objects.all()
	data={'online':online}
	return render(request, 'online.html',data)

def offlin(request):
	offline=offlinetraining.objects.all()
	data={'offline':offline}
	return render(request, 'offline.html',data)

def staffd(request):
	return render(request, 'staffdetails.html')

def maint(request):
	return render(request, 'maintra.html')





def admintrainee(request):
	return render(request, 'adm_trainee.html')

def admintrainer(request):
	return render(request, 'adm_trainer.html')

def admintimetable(request):
	return render(request, 'adm_timetable.html')

def admin_view_timetable(request):
	return render(request, 'adm_view_timetable.html')

def admin_edit_timetable(request):
	return render(request, 'adm_edit_timetable.html')

def admin_userpayment(request):
	return render(request, 'adm_viewpayment.html')

def admin_view_userpay(request):
	return render(request, 'adm_view_userpayment.html')

def admin_payment(request):
	return render(request, 'adm_payment.html')

def admin_pay_page(request):
	return render(request, 'adm_pay_page.html')