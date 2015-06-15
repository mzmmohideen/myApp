from django.db import models
from django.contrib.auth.models import *

class User_details(models.Model):
	uname = models.OneToOneField(User)
	# nickname = models.CharField(max_length = 40)
	message = models.CharField(max_length = 140)
	send_to = models.CharField(max_length = 40)
	# passwd = models.OneToOneField(User)
# Create your models here.
