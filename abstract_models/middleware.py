

from django.http import JsonResponse


class SampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view execution")
        response = self.get_response(request)
        print("After view execution")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs ):
        
        print("process_view Worked")
        return JsonResponse({
            "status":True,
            "message":"Middlware worked",
        })
    