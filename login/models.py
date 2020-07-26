from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from __future__ import unicode_literals



class tt(models.Model):
	sem_no=models.IntegerField();
	branch=models.IntegerField();

	def __str__(self):
		return self.sem_no

class Past_scholars(models.Model):
	name = models.CharField(max_length=100,blank=False)
	linkedin = models.CharField(max_length=100,blank=False)

class Opp(models.Model):
	name = models.CharField(max_length=100, blank=False)
	links = models.CharField(max_length=100, blank=False)
	gen_date = models.DateField()
	past = models.ManyToManyField(Past_scholars)

	def __str__(self):
		return self.name


class Sender(models.Model):
    sender_id = models.TextField()
    topic = models.TextField()

class Memory(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    key = models.TextField()
    value = models.TextField()

class Conversation(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    message = models.TextField()


# class Profile(models.Model):
# 	user = model.OneToOneField(User, on_delete=models.CASCADE)
# 	branch = user.username()




# Create your models here.
