from django.urls import path
from .views import BaseAPIView
# import as_view() from django.views.generic
# from django.views.generic import as_view

urlpatterns = [
    path('', BaseAPIView.as_view(), name='base'),
]