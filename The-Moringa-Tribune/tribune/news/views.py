from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404#import the httpresponse class from the django.http module reposible for returning reponse to the user.
import datetime as dt

# Create your views here.
def welcome(request):#takes the request argument
	return render(request,'welcome.html')

#deleted the date function since all of that is now defined with the date filter

def news_today(request):
	date = dt.date.today()
	return render(request,'all-news/today-news.html',{"date":date,})#pass in 3 arguments last one is a dictionary of values that we want to pass into the template the dictionary is referred to as the context in django

def past_days_news(request,past_date):

	try:
		# Converts data from the string Url
		date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
		
	except ValueError:
		#Raise 404 error when ValueError is thrown
		raise Http404()
		assert False 

	if date == dt.date.today():
		return redirect(news_today)
		
	return render(request,'all-news/past-news.html',{"date":date})
