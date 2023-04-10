
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
        print("URL ",request.path)
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
        return None