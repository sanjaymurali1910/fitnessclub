import os
import random
from django.shortcuts import render, redirect
from fitnessproapp.models import *
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.db.models import Q
from fitnesspro.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.



# login page

def login(request):

    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'admhome')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="trainer").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tnr_id'] = member.id
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'maintra.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="trainee").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tne_id'] = member.id
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'index.html',{'mem1':mem1})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')





#  Forgot password


def Forgot_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.filter(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)
            print(password)
            _user.update(password = password)
            subject =' your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)
            #_user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Forgot_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist  "
            return render(request, 'Forgot_password.html', {'msg_error': msg_error})
    return render(request,'Forgot_password.html')



# signup page

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




# user side functions(trainee)

def User_profile(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        return render(request,'User_profile.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_edit_profile(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        pro = user_registration.objects.get(id=Tne_id)
        if request.method=='POST':
            usrs = user_registration.objects.get(id=Tne_id)
            usrs.firstname = request.POST.get('u_name')
            usrs.lastname = request.POST.get('pincode')
            usrs.email = request.POST.get('district')
            usrs.password = request.POST.get('state')
            usrs.save()
            return redirect('User_profile')
        return render(request,'User_edit_profile.html',{'mem1':mem1,'pro':pro})
    else:
        return redirect('/')

def index(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'index.html',{'mem1':mem1})
	else:
		return redirect('/')	




def about(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'about-us.html',{'mem1':mem1})
	else:
		return redirect('/')		




def classes(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'classes.html',{'mem1':mem1})
	else:
		return redirect('/')		




def train(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		tra=user_registration.objects.filter(status='trainer')
		return render(request, 'Trainer.html',{'tra':tra,'mem1':mem1})
	else:
		return redirect('/')		




def selecttrainer(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'selecttrainer.html',{'mem1':mem1})
	else:
		return redirect('/')		




def shedule(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		timetable=batch.objects.all()
		data={'timetable':timetable,'mem1':mem1}
		return render(request, 'timetable.html',data)
	else:
		return redirect('/')		




def contact(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'contact.html',{'mem1':mem1})   
	else:
		return redirect('/')		





def userpaymentpage(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		if request.method=='POST':
			sn=request.POST['name']
			n=request.POST['bankname']
			an=request.POST['accnumber']
			ifsc=request.POST['ifsccode']
			am=request.POST['amount']
			date = datetime.now()
			paymenttrainee.objects.create(sname=sn,name=n,accountnumber=an,ifsc=ifsc,payment=am,date=date)
			msg_success = "Payment successfully Completed"
			return render(request, 'user_pay_page.html', {'msg_success': msg_success})
		return render(request, 'user_pay_page.html',{'mem1':mem1})
	else:
		return redirect('/')





def online_training(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		if request.method=='POST':
			fn=request.POST['fname']
			ln=request.POST['lname']
			e=request.POST['email']
			p=request.POST['plan']
			onlinetraining.objects.create(firstname=fn,lastname=ln,email=e,plan=p)
			return redirect('userpaymentpage')
		return render(request, 'online_training.html',{'mem1':mem1})
	else:
		return redirect('/')		





def offline_training(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)	
		if request.method=='POST':
			fn=request.POST['fname']
			ln=request.POST['lname']
			e=request.POST['email']
			p=request.POST['plan']
			offlinetraining.objects.create(firstname=fn,lastname=ln,email=e,plan=p)
			return redirect('userpaymentpage') 
		return render(request, 'offline_training.html',{'mem1':mem1})
	else:
		return redirect('/')





def Trainee_logout(request):
    if 'Tne_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')		

# user side end
  


# trainer side functions



def onlin(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		online=onlinetraining.objects.all()
		data={'online':online,'mem':mem}
		return render(request, 'online.html',data)
	else:
		return redirect('/')





def onedit(request,i_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		oned=onlinetraining.objects.get(id=i_id)
		return render(request,'online_edit.html',{'oned':oned,'mem':mem})
	else:
		return redirect('/')	





def onlineedit(request,oned_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		if request.method=='POST':
			oneds=onlinetraining.objects.get(id=oned_id)
			oneds.firstname=request.POST.get('first_name')
			oneds.lastname=request.POST.get('last_name')
			oneds.email=request.POST.get('email')
			oneds.status=request.POST.get('status')
			oneds.save()
			subject = 'FitnrssClub Joining Details'
			message = 'Dear Friend,\nWe are pleased to inform that your request to join our online class is approved\nYour online class link is here:https://meet.google.com/rnz-hvbo-eeb'
			recipient = oneds.email
			send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
			messages.success(request, 'Success!')
			return redirect('onlin')

		return render(request,'online_edit.html',{'mem':mem})
	else:
		return redirect('/')





def offlin(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		offline=offlinetraining.objects.all()
		data={'offline':offline,'mem':mem}
		return render(request, 'offline.html',data)
	else:
		return redirect('/')		





def offedit(request,i_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		offd=offlinetraining.objects.get(id=i_id)
		return render(request,'offline_edit.html',{'offd':offd,'mem':mem})
	else:
		return redirect('/')





def offlineedit(request,offd_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		if request.method=='POST':
			offds=offlinetraining.objects.get(id=offd_id)
			offds.firstname=request.POST.get('first_name')
			offds.lastname=request.POST.get('last_name')
			offds.email=request.POST.get('email')
			offds.status=request.POST.get('status')
			offds.save()
			subject = 'FitnrssClub Joining Details'
			message = 'dear Friend,\nWe are pleased to inform that your request to join our online class is approved'
			recipient = offds.email
			send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
			messages.success(request, 'Success!')
			return redirect('offlin')

		return render(request,'offline_edit.html',{'mem':mem})
	else:
		return redirect('/')	






def staffd(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		paydata=paymenttrainer.objects.all()
		data={'paydata':paydata,'mem':mem}
		return render(request, 'staffdetails.html',data)
	else:
		return redirect('/')		





def maint(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		return render(request, 'maintra.html',{'mem':mem})
	else:
		return redirect('/')	



def Usert_profile(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        return render(request,'Usert_profile.html',{'mem':mem})
    else:
        return redirect('/')

def Usert_edit_profile(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        pro = user_registration.objects.get(id=Tnr_id)
        if request.method=='POST':
            usrs = user_registration.objects.get(id=Tnr_id)
            usrs.firstname = request.POST.get('u_name')
            usrs.lastname = request.POST.get('pincode')
            usrs.email = request.POST.get('district')
            usrs.password = request.POST.get('state')
            usrs.save()
            return redirect('Usert_profile')
        return render(request,'Usert_edit_profile.html',{'mem':mem,'pro':pro})
    else:
        return redirect('/')




def Trainer_logout(request):
    if 'Tnr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')	


# trainer side end



#admin side functions



def admhome(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		return render(request, 'adm_home.html',{'users':users})
	else:
		return redirect('/')





def admreg(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		det=user_registration.objects.all()
		data={'det':det,'users':users}
		return render(request, 'adm_reg.html',data)
	else:
		return redirect('/')		





def admregedit(request,i_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		reg=user_registration.objects.get(id=i_id)
		return render(request, 'adm_regedit.html',{'reg':reg,'users':users})
	else:
		return redirect('/')		






def admregistration(request,reg_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			regs=user_registration.objects.get(id=reg_id)
			regs.firstname=request.POST.get('first_name')
			regs.lastname=request.POST.get('last_name')
			regs.email=request.POST.get('email')
			regs.status=request.POST.get('status')
			regs.save()
			subject = 'FitnessClub Welcome Message'
			message = 'dear Friend,\nWe welcome you to Fitnessclub'
			recipient = regs.email
			send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
			messages.success(request, 'Success!')
			return redirect('admreg')

		return render(request,'adm_regedit.html',{'users':users})
	else:
		return redirect('/')






def admintimetable(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			d=request.POST['day']
			ft=request.POST['fromtime']
			tt=request.POST['totime']
			w=request.POST['workout']
			wc=request.POST['workcate']
			batch.objects.create(day=d,fromtime=ft,totime=tt,workout=w,workoutcate=wc)
		return render(request, 'adm_timetable.html',{'users':users})
	else:
		return redirect('/')		






def admin_view_timetable(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		timetable=batch.objects.all()
		data={'timetable':timetable,'users':users}
		return render(request, 'adm_view_timetable.html',data)
	else:
		return redirect('/')






def admin_edit_timetable(request,i_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		timet=batch.objects.get(id=i_id)
		return render(request, 'adm_edit_timetable.html',{'timet':timet,'users':users})
	else:
		return redirect('/')		





def admin_editpage(request,timet_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			table = batch.objects.get(id=timet_id)
			table.day=request.POST.get('day')
			table.fromtime=request.POST.get('fromtime')
			table.totime=request.POST.get('totime')
			table.workout=request.POST.get('workout')
			table.workoutcate=request.POST.get('workcate')
			table.save()
			return redirect('admin_view_timetable')
		return render(request, 'adm_edit_timetable.html',{'users':users})
	else:
		return redirect('/')






def delete_batch(request,p_id):
	products=batch.objects.get(id=p_id)
	products.delete()
	return redirect('admin_view_timetable')







def admin_userpayment(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		paydata=paymenttrainee.objects.all()
		data={'paydata':paydata,'users':users}
		return render(request, 'adm_viewpayment.html',data)
	else:
		return redirect('/')







def admin_payment(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		paydata=paymenttrainer.objects.all()
		data={'paydata':paydata,'users':users}
		return render(request, 'adm_payment.html',data)
	else:
		return redirect('/')		








def admin_pay_page(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			n=request.POST['bankname']
			an=request.POST['accnumber']
			ifsc=request.POST['ifsccode']
			am=request.POST['amount']
			date = datetime.now()
			paymenttrainer.objects.create(name=n,accountnumber=an,ifsc=ifsc,payment=am,date=date)
			msg_success = "Payment successfully Completed"
			return render(request, 'adm_pay_page.html', {'msg_success': msg_success})
		return render(request, 'adm_pay_page.html',{'users':users})
	else:
		return redirect('/')		 






def SuperAdmin_logout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/')