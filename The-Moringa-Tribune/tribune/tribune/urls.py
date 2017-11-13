"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include#ubckyde funtion allows us to reference another urlconf 
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),#r character tells python this is a raw string and shouldn't interpret backslashes the same way as a normal string 
    url(r'^news/',include('news.urls'))#create a new regex and call include with no ending string but a trailing forward slash when django encounters the include function it will chop off whatever part of the URL that matched till the point and send the rest to the referenced URLconf.    
]
