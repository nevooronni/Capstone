from django.shortcuts import render
from django.conf.urls import url 
from django.http import HttpResponse

def index(request):
	return render(request,'index.html')
