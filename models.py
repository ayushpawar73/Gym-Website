from pickle import TRUE
from django.db import models
from .models import*
 
class feedback(models.Model):
     firstname=models.CharField(max_length=50,null=True)
     lastname=models.CharField(max_length=50,null=True)
     mail_id=models.CharField(max_length=50,null=True)
     country=models.CharField(max_length=50,null=True)
     feedback=models.CharField(max_length=50,null=True)

class pricing(models.Model):
     silver=models.CharField(max_length=50,null=True)
     gold=models.CharField(max_length=50,null=True)
     diamond=models.CharField(max_length=50,null=True)

class userdata(models.Model):
     firstname=models.CharField(max_length=50,null=True)
     lastname=models.CharField(max_length=50,null=True)
     gender=models.CharField(max_length=50,null=True)
     lbs=models.CharField(max_length=50,null=True)
     weight=models.CharField(max_length=500,null=True)
     height=models.CharField(max_length=200,null=True)
     address=models.CharField(max_length=200,null=True)
     city=models.CharField(max_length=50,null=True)
     state=models.CharField(max_length=50,null=True)
     zipcode=models.CharField(max_length=50,null=True)
     firstname=models.CharField(max_length=50,null=True)
     country=models.CharField(max_length=50,null=True)
     email=models.CharField(max_length=50,null=True)
     phoneno=models.CharField(max_length=50,null=True)
     plan=models.CharField(max_length=50,null=True)

class participantname(models.Model):
     pname=models.CharField(max_length=50,null=True)