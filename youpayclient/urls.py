from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('youpayclient.v1.urls')),
]
