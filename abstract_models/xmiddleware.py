
from rest_framework.response  import Response
from django.http import JsonResponse

class SampleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Middleware init")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Middleware call before request")
        response = None
        
        flag = False
        
        if flag :
            # response = Response({
            #     "status": "error",
            # })
            # # self.process_request(request)
            # response = self.get_response(request)
            # return response
        
            return JsonResponse({'error': 'Some error'}, status=401)
            
        
        else:
            response = self.get_response(request)

        # print("Middleware call after request ",response)
        # print("Middleware call after request ",response.data.keys())
        # print("Middleware call after request ",response.data['message'])
        # print("URL ",request.path)
        # also need to check request type ie post or get
        
        payment_paths = [
            "abstract_models/"
        ]
        if request.path in payment_paths:
            print("Found Payment Path")
            #update attempt count in Transaction table

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_request(self, request):
        print("process_request")
        print("request", request)
        return None

    def process_response(self, request, response):
        print("process_response")
        print("response", response)
        return response

    def process_exception(self, request, exception):
        print("process_exception")
        print("exception", exception)
        return None
    
    def process_view(self, request, view_func, view_args, view_kwargs ):
        
        print("process_view Worked")
        return JsonResponse({
            "status":True,
            "message":"Middlware worked",
        })
    

# from functools import wraps
# from django.utils.decorators import available_attrs

# def my_middleware_decorator(view_class):
#     def _middleware_wrapper(view_func):
#         @wraps(view_func, assigned=available_attrs(view_func))
#         def _wrapped_view(request, *args, **kwargs):
#             # Call the middleware
#             middleware = SampleMiddleware(view_func)
#             response = middleware(request)
#             # If the middleware returns a response, return it immediately
#             if response is not None:
#                 return response
#             # Otherwise, call the view function
#             return view_func(request, *args, **kwargs)

#         return _wrapped_view
    
#     # Check if the decorator is being applied to the specific class-based view
#     if isinstance(view_class, type) and issubclass(view_class, View):
#         view_class.dispatch = my_middleware_decorator(view_class.dispatch)
        
#     return _middleware_wrapper



# from django.utils.decorators import decorator_from_middleware

# simple_decorator = decorator_from_middleware(SampleMiddleware)
# class SimpleMiddlewareMixin:
#     @simple_decorator 
#     def dispatch(*args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    
    

