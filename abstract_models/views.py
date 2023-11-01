from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response  import Response
from rest_framework.views import APIView
from django.db import transaction

# from abstract_models.middleware import SampleMiddleware
# from abstract_models.middleware import my_middleware_decorator

# from abstract_models.models import ModelA
# from abstract_models.serializers import ModelASerializers
# from django.views.generic import View

from django.utils.decorators import method_decorator
from .models import Base, ModelA


# @method_decorator(SampleMiddleware,name="dispatch")
# Create your views here.
class BaseAPIView(ListAPIView):
    """
    Base class for all API views
    """
    def get(self, request):
        """
        GET request
        """
        print("GET BASEAPIVIEW Worked")
        return Response(status=200, data={'message': 'Hello World'})

    def post(self, request):
        """
        POST request
        """
        data = self.request.data
        
        try:
        # print("\n\n\nPOST METHOD WORKED : {}".format(self.request.data) )
            
            print("\n\n\nDATA payment_status : {}, is_fraud : {} is_flagged : {}".format(data.payment_status,
data.is_fraud,
data.is_flagged))
            
        except Exception as e:
            print("Excepction occured for data : \n{}".format(data))
        
        # data = request.data
        # # print(data)
        # # data = {
        # #     'level': data['level'],
        # # }
        # try:
        #     serializer = ModelASerializers(data=data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #         # ModelA.objects.create(**data)
        #         return Response(status=201, data=serializer.data)
        # except Exception as e:
        #     if serializer.errors:
        #         return Response(status=400, data=serializer.errors)    
        #     return Response(status=400, data={'message': str(e)})
        return Response({
            "status":True,
            "message":"POST BaseAPIView"
        })

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

# @simple_decorator
# @my_middleware_decorator(ProApiView)


# function to add 2 array


# Attempt 2 Start
from django.utils.decorators import method_decorator
from abstract_models.middleware import SampleMiddleware

@method_decorator(SampleMiddleware, name='dispatch')
class ProApiView(ListAPIView):
    def get(self,request):
        print("GET PROAPIVIEW Worked")
        
        return Response({
            "Status":True,
            "message":"GET ProApiView Worked"
        })
        
    # @simple_decorator  
    def post(self,request):
        print("PSOT PROAPIVIEW Worked")
        
        return Response({
            "Status":True,
            "message":"POST ProApiView Worked"
        })
        
        
#Attempt 3 start
from abstract_models.class_based_middleware import ClassAMiddleware, ClassBMiddleware

from abstract_models.decoratorbaseMiddleware import middleware_check_decorator

# @middleware_check_decorator
class ClassA(ListAPIView):
    # Apply the ClassAMiddleware to the middleware attribute
    middleware = [ClassAMiddleware]
    def get(self, request):
        """
        GET request
        """
        print("GET BASEAPIVIEW Worked")
        return Response(status=200, data={'message': 'Hello World'})

    def post(self, request):
        """
        POST request
        """
        print("POST BASEAPIVIEW Worked")
        return Response({
            "status":True,
            "message":"POST BaseAPIView"
        })

class ClassB(ListAPIView):
    # Apply the ClassBMiddleware to the middleware attribute
    middleware = [ClassBMiddleware]
    def get(self,request):
        print("GET PROAPIVIEW Worked")
        
        return Response({
            "Status":True,
            "message":"GET ProApiView Worked"
        })
        
    # @simple_decorator  
    def post(self,request):
        print("PSOT PROAPIVIEW Worked")
        
        return Response({
            "Status":True,
            "message":"POST ProApiView Worked"
        })
        
class DecoratorBasedMiddlewareSample(ListAPIView):
    def get(self,request):
        print("GET DecoratorBasedMiddlewareSample Worked")
        
        return Response({
            "Status":True,
            "message":"GET DecoratorBasedMiddlewareSample Worked"
        })
        
class ClassTransaction(APIView):
    def post(self,request):
        msg = "Post ClassTransaction Worked"
        print(msg)
        with transaction.atomic():
            # print("Base ",Base.objects.all())        
            model_obj = ModelA.objects.select_for_update().first()
            print("Model obj before",model_obj.name)
            if model_obj.name == "two":
                model_obj.name = "one"
            else:
                model_obj.name = "two"
            model_obj.save()
        print("Model obj after",model_obj.name)
        
        
        return Response({
            "Status":True,
            "message":msg
        })
        