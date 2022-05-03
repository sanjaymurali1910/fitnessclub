from django.db import models

# Create your models here.
class onlinetraining(models.Model):
    firstname = models.CharField(max_length=240, null=True) 
    lastname = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    plan = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='New')

    def __str__(self):
        return self.firstname

class offlinetraining(models.Model):
    firstname = models.CharField(max_length=240, null=True) 
    lastname = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    plan = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='New')

    def __str__(self):
        return self.firstname

class paymenttrainee(models.Model):                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.CharField(max_length=240, null=True)
    name = models.CharField(max_length=240, null=True)
    sname = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifsc = models.CharField(max_length=240, null=True)

class paymenttrainer(models.Model):                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.CharField(max_length=240, null=True)
    name = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifsc = models.CharField(max_length=240, null=True)

class batch(models.Model): 
    day = models.CharField(max_length=100)
    fromtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    totime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    workout = models.CharField(max_length=100)
    workoutcate = models.CharField(max_length=100)

    def __str__(self):
        return self.day

class user_registration(models.Model):

    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    password = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='trainee')


    def __str__(self):
        return self.firstname