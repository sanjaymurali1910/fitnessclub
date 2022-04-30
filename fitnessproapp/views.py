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
from fitnesspro.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.

def login(request):

    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'SuperAdmin_Dashboard')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="trainer").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tnr_id'] = member.id
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'Trainer_dashboard.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="trainee").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tne_id'] = member.id
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'Trainee_dashboard.html',{'mem1':mem1})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        acc = user_registration()
        acc.firstname = request.POST['first_name']
        acc.lastname = request.POST['last_name']
        acc.username = request.POST['username']
        acc.email = request.POST['email']
        acc.photo = request.FILES['file']
        acc.password = request.POST['password']
        acc.save()
    return render(request,'signup.html')


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
	timetable=batch.objects.all()
	data={'timetable':timetable}	
	return render(request, 'timetable.html',data)

def contact(request):
	return render(request, 'contact.html')   

def join(request):
	return render(request, 'join.html')



def userpaymentpage(request):
	if request.method=='POST':
		sn=request.POST['name']
		n=request.POST['bankname']
		an=request.POST['accnumber']
		ifsc=request.POST['ifsccode']
		am=request.POST['amount']
		date = datetime.now()

		paymenttrainee.objects.create(sname=sn,name=n,accountnumber=an,ifsc=ifsc,payment=am,date=date)

	return render(request, 'user_pay_page.html')


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

def onedit(request,i_id):
	oned=onlinetraining.objects.get(id=i_id)
	return render(request,'online_edit.html',{'oned':oned})
	
def onlineedit(request,oned_id):
	if request.method=='POST':
		oneds=onlinetraining.objects.get(id=oned_id)
		oneds.firstname=request.POST.get('first_name')
		oneds.lastname=request.POST.get('last_name')
		oneds.email=request.POST.get('email')
		oneds.status=request.POST.get('status')
		oneds.save()
		subject = 'Internship Python'
		message = 'dear Candidate,\nWe are pleased to inform that you are selected our 6 months free inernship program..'
		recipient = oneds.email
		send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
		messages.success(request, 'Success!') 
		return redirect('onlin')
	return render(request,'online_edit.html')	


def offlin(request):
	offline=offlinetraining.objects.all()
	data={'offline':offline}
	return render(request, 'offline.html',data)

def offedit(request,i_id):
	offd=offlinetraining.objects.get(id=i_id)

	return render(request,'offline_edit.html',{'offd':offd})



def staffd(request):
	paydata=paymenttrainer.objects.all()
	data={'paydata':paydata}	
	return render(request, 'staffdetails.html',data)

def maint(request):
	return render(request, 'maintra.html')




def admhome(request):
	return render(request, 'adm_home.html')

def admreg(request):
	det=user_registration.objects.all()
	data={'det':det}
	return render(request, 'adm_reg.html',data)

def admregedit(request,i_id):
	reg=user_registration.objects.get(id=i_id)
	return render(request, 'adm_regedit.html',{'reg':reg})

def admregistration(request,reg_id):
	if request.method=='POST':
		regs=user_registration.objects.get(id=reg_id)
		regs.firstname=request.POST.get('first_name')
		regs.lastname=request.POST.get('last_name')
		regs.email=request.POST.get('email')
		regs.status=request.POST.get('status')
		regs.save()
		subject = 'Internship Python'
		message = 'dear Candidate,\nWe are pleased to inform that you are selected our 6 months free inernship program..'
		recipient = regs.email
		send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
		messages.success(request, 'Success!') 
		return redirect('admreg')

	return render(request,'adm_regedit.html')


def admintrainee(request):
	return render(request, 'adm_trainee.html')

def admintrainer(request):
	return render(request, 'adm_trainer.html')

def admintimetable(request):
	if request.method=='POST':
		d=request.POST['day']
		ft=request.POST['fromtime']
		tt=request.POST['totime']
		w=request.POST['workout']
		wc=request.POST['workcate']

		batch.objects.create(day=d,fromtime=ft,totime=tt,workout=w,workoutcate=wc)
	return render(request, 'adm_timetable.html')

def admin_view_timetable(request):
	timetable=batch.objects.all()
	data={'timetable':timetable}

	return render(request, 'adm_view_timetable.html',data)

def admin_edit_timetable(request,i_id):
	timet=batch.objects.get(id=i_id)
	return render(request, 'adm_edit_timetable.html',{'timet':timet})

def admin_editpage(request,timet_id):
	if request.method=='POST':
		table = batch.objects.get(id=timet_id)
		table.day=request.POST.get('day')
		table.fromtime=request.POST.get('fromtime')
		table.totime=request.POST.get('totime')
		table.workout=request.POST.get('workout')
		table.workoutcate=request.POST.get('workcate')
		table.save()
		return redirect('admin_view_timetable')

 
	return render(request, 'adm_edit_timetable.html')


def delete_batch(request,p_id):
    products=batch.objects.get(id=p_id)
    products.delete()

    return redirect('admin_view_timetable')

def admin_userpayment(request):
	paydata=paymenttrainee.objects.all()
	data={'paydata':paydata}
	return render(request, 'adm_viewpayment.html',data)


def admin_view_userpay(request):
	return render(request, 'adm_view_userpayment.html')

def admin_payment(request):
	paydata=paymenttrainer.objects.all()
	data={'paydata':paydata}	
	return render(request, 'adm_payment.html',data)

def admin_pay_page(request):
	if request.method=='POST':
		n=request.POST['bankname']
		an=request.POST['accnumber']
		ifsc=request.POST['ifsccode']
		am=request.POST['amount']
		date = datetime.now()

		paymenttrainer.objects.create(name=n,accountnumber=an,ifsc=ifsc,payment=am,date=date)

	return render(request, 'adm_pay_page.html')