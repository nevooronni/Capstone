from django.shortcuts import render
from django.conf.urls import url 
from django.http import HttpResponse

def welcome(request):
	return HttpResponse('welcome to the Moringa Tribune')
