

from django.http import JsonResponse


class DecoratorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Middleware init")
    
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.       
        print("Decorator based Middleware")       
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # middleware decorator name check
        middleware_check_decorator = getattr(view_func,'middleware_check_decorator', False)
        if middleware_check_decorator:
            return JsonResponse({"message":"decorator middleware triggered"})


from django.utils.decorators import decorator_from_middleware, classonlymethod
#middleware_check_decorator this can be used in any view to check related one
middleware_check_decorator = decorator_from_middleware(DecoratorMiddleware)

class PaymentStatusCheckMiddlewareMixin:
    @middleware_check_decorator
    def dispatch(*args, **kwargs):
        return super().dispatch(*args, **kwargs)


def middleware_check_decorator(class_view):
    def as_view(cls, **initkwargs):
        view = super(cls, cls).as_view(**initkwargs)
        view.middleware_check_decorator = True
        return view

    return type(class_view.__name__, (class_view,), {
        'as_view': classonlymethod(as_view),
    })



class PathBasedMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Middleware init")
    
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        print("Path based Middleware")
     
        payment_paths = [
            "abstract_models/"
        ]
        if request.path in payment_paths:
            print("Found Payment Path")
            #update attempt count in Transaction table

        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)

        return response
    

