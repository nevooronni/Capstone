from django.conf.urls import url#import url function
from . import views#import app views 


urlpatterns=[
	url('^$',views.welcome,name = 'welcome'),
	url('^today/$',views.news_today,name = 'newToday'),
	url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')#capture our regex and send it to our view function 
]#create a list named urlpatterns will be a list of our url instances of our app a url function passes in 4 arguments two are required the regular expression and view other two are optional 