# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)
	content = models.TextField()
	# def __unicode__(self):
	# 	return self.title

