from django.utils.deprecation import MiddlewareMixin

class ClassAMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # from abstract_models.views import A
        
        # if issubclass(view_func.view_class, A):
        class_name_list = ['ClassA']
        if request.resolver_match.view_name in class_name_list:
            # Code to be executed before the view
            # ...
            print("Class A Middleware")

            # Call the view function
            response = view_func(request, *view_args, **view_kwargs)

            # Code to be executed after the view
            # ...

            return response

class ClassBMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        # from abstract_models.views import B
        
        # if issubclass(view_func.view_class, B): #this will check if view_func is instance of B so for admin it will not work
        class_name_list = ['ClassB']
        if request.resolver_match.view_name in class_name_list:
            
            # Code to be executed before the view
            # ...
            print("Class B Middleware")
            # Call the view function
            response = view_func(request, *view_args, **view_kwargs)

            # Code to be executed after the view
            # ...

            return response

