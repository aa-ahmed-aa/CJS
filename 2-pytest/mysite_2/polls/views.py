# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from datetime import time
from django.http import HttpResponse
from .greeter import greeting_at

def greet(request):
	now = datetime.now().time()
	greeting = greeting_at(now)
	reurn HttpResponse('Good %s!' % greeting)