from django.urls import path
from .views import BaseAPIView, ProApiView, ClassA, ClassB, ClassTransaction
# import as_view() from django.views.generic
# from django.views.generic import as_view

urlpatterns = [
    path('', BaseAPIView.as_view(), name='base'),
    path('pro/', ProApiView.as_view(), name='pro'),
    path('a/', ClassA.as_view(), name='ClassAx'),
    path('b/', ClassB.as_view(), name='ClassA'),
    path('transaction-check/', ClassTransaction.as_view(), name='ClassA'),
]