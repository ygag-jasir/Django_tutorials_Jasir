"""django_tutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from abstract_models.views import BaseAPIView

from customizeAdmin.views import QitafResponseSimulator

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('abstract_models/', include('abstract_models.urls')),
    
    path('tabbypg/', include('tabbypgclient.urls')),
        
    path('youpay/', include(('youpayclient.urls', 'youpayclient'), namespace='youpay-webhook')),
    
    path('qitaf-test/', QitafResponseSimulator.as_view(), name='qitaf-response-simulator'),
    
    path('webhook-receive/',BaseAPIView.as_view()),
    
    path('whitelabelDemo/', include('whitelabelDemo.urls')),
         
]
