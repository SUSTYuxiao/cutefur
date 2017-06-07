from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

# Create your models here.
class Hardware(models.Model):
	name_id = models.CharField(max_length = 150)
	state = models.BooleanField()

admin.site.register(Hardware)

#tongjishuju
class tjsj(models.Model):
	name = models.CharField(max_length=32, primary_key=True)
	ydl_data = models.IntegerField(default=0)
	snwd_data = models.IntegerField(default=0)
	snsd_data = models.IntegerField(default=0)
	ysl_data = models.IntegerField(default=0)