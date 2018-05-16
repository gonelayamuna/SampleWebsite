# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from .models import Blog
def blog(request):
	blog = Blog.objects.all()
	return render(request,'blog.html',{'blog':blog})
