from django.db import models

# Create your models here.
class onlinetraining(models.Model):
    firstname = models.CharField(max_length=240, null=True) 
    lastname = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)

    def __str__(self):
        return self.firstname

class offlinetraining(models.Model):
    firstname = models.CharField(max_length=240, null=True) 
    lastname = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)

    def __str__(self):
        return self.firstname
