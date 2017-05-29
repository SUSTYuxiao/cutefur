from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

# Create your models here.
class Hardware(models.Model):
	name_id = models.CharField(max_length = 150)
	state = models.BooleanField()

admin.site.register(Hardware)

