from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.
class customer(models.Model):
	cid          = models.IntegerField(primary_key=True,default=1)
	email        = models.EmailField(default='kalyanshiva98@gmail.com')
	username     = models.CharField(max_length=1024,default='kalyanshiva')
	cname        = models.CharField(max_length=1024)
	phone_number = PhoneNumberField()
	address      = models.CharField("Address line 1",max_length=1024)
	password     = models.CharField(max_length=50)
	object       = models.Manager()
  
class bookings(models.Model):
	cid          = models.ForeignKey('customer', on_delete=models.CASCADE)
	bid          = models.IntegerField(primary_key=True,default=1)
	aid          = models.ForeignKey('accomodation', on_delete=models.CASCADE)
	rid          = models.ForeignKey('restaraunt', on_delete=models.CASCADE,default=1)
	tid          = models.ForeignKey('transportation', on_delete=models.CASCADE)
	pno          = models.ForeignKey('package', on_delete=models.CASCADE,default=1)
	Date         = models.DateField(default=date.today)
	
class accomodation(models.Model):
	aid          = models.IntegerField(primary_key=True,default=1)
	location     = models.CharField(max_length=1024)
	atype        = models.CharField(max_length=1024)
	name         = models.CharField(max_length=1024)

class transportation(models.Model):
	tid          = models.IntegerField(primary_key=True,default=1)

class package(models.Model):
	pno          = models.IntegerField(primary_key=True,default=2)
	pcost        = models.IntegerField(default=1)
	noofpass     = models.IntegerField(default=1)
	pname        = models.CharField(max_length=1024)

class placeby(models.Model):
	pid          = models.IntegerField(primary_key=True,default=1)
	name         = models.CharField(max_length=1024)
	description  = models.TextField(default='INDIA')

class events(models.Model):
	eid          = models.IntegerField(primary_key=True,default=1)
	name         = models.CharField(max_length=1024)
	startDate    = models.DateField(default=date.today)
	endDate      = models.DateField(default=date.today)
	etype        = models.CharField(max_length=1024)
	starttime    = models.TimeField(auto_now_add=True)
	endtime      = models.TimeField(auto_now_add=True)

class restaraunt(models.Model):
	rid          = models.IntegerField(primary_key=True,default=1)
	name         = models.CharField(max_length=1024)
	rtype        = models.CharField(max_length=1024)
	starttime    = models.TimeField(auto_now_add=True)
	endtime      = models.TimeField(auto_now_add=True)
	location     = models.CharField(max_length=1024)

class reserve(models.Model):
	aid          = models.ForeignKey('accomodation', on_delete=models.CASCADE)
	tid          = models.ForeignKey('transportation', on_delete=models.CASCADE)
	rid          = models.ForeignKey('restaraunt', on_delete=models.CASCADE)


class airway(models.Model):
	aiid          = models.IntegerField(primary_key=True,default=1) 
	area          = models.CharField(max_length=1024)	
	aclass        = models.CharField(max_length=1024)
	name          = models.CharField(max_length=1024,default='air india')

class roadway(models.Model):
	roid          = models.IntegerField(primary_key=True,default=1)  
	area          = models.CharField(max_length=1024)	
	rotype        = models.CharField(max_length=1024)
	name          = models.CharField(max_length=1024,default='morning star')

class waterway(models.Model):
	wid           = models.IntegerField(primary_key=True,default=1)  
	area          = models.CharField(max_length=1024)	
	wclass        = models.CharField(max_length=1024)
	name          = models.CharField(max_length=1024,default='Titanic')

class eventsof(models.Model):
	eid          = models.ForeignKey('events', on_delete=models.CASCADE)
	pid          = models.ForeignKey('placeby', on_delete=models.CASCADE)

class accomodationfor(models.Model):
	aid          = models.ForeignKey('accomodation', on_delete=models.CASCADE)
	pid          = models.ForeignKey('placeby', on_delete=models.CASCADE)

class transportationfor(models.Model):
	tid          = models.ForeignKey('transportation', on_delete=models.CASCADE)
	pid          = models.ForeignKey('placeby', on_delete=models.CASCADE)
		
class payment(models.Model):
	mode         = models.CharField(primary_key=True,max_length=1024)
	eprice       = models.IntegerField(default=1)
	oprice       = models.IntegerField(default=1)
	name         = models.CharField(max_length=1024)


class payby(models.Model):
	pid          = models.ForeignKey('placeby', on_delete=models.CASCADE)
	pno	         = models.ForeignKey('package', on_delete=models.CASCADE)	
	mode         = models.ForeignKey('payment', on_delete=models.CASCADE)	