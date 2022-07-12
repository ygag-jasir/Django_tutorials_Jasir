from django.shortcuts import render

# Create your views here.
class BaseAPIView(object):
    """
    Base class for all API views
    """
    def get(self, request):
        """
        GET request
        """
        return render(request, 'base.html')

    def post(self, request):
        """
        POST request
        """
        return render(request, 'base.html')

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