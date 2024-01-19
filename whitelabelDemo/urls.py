from django.urls import path
from .views import WhiteLabelView
# import as_view() from django.views.generic
# from django.views.generic import as_view

urlpatterns = [
    path('', WhiteLabelView, name='white-label'),
    
]