from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response  import Response

from abstract_models.models import ModelA
from abstract_models.serializers import ModelASerializers
# Create your views here.
class BaseAPIView(ListAPIView):
    """
    Base class for all API views
    """
    def get(self, request):
        """
        GET request
        """
        return Response(status=200, data={'message': 'Hello World'})

    def post(self, request):
        """
        POST request
        """
        data = request.data
        # print(data)
        # data = {
        #     'level': data['level'],
        # }
        try:
            serializer = ModelASerializers(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # ModelA.objects.create(**data)
                return Response(status=201, data=serializer.data)
        except Exception as e:
            if serializer.errors:
                return Response(status=400, data=serializer.errors)    
            return Response(status=400, data={'message': str(e)})


    def put(self, request):
        """
        PUT request
        """
        return render(request, 'base.html')

    def delete(self, request):
        """
        DELETE request
        """
        return render(request, 'base.html')



# function to add 2 array