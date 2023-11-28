
class WhiteLabelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract subdomain from the request
        parts = request.get_host().split('.')
        if len(parts) > 2:
            subdomain = parts[0]
            request.subdomain = subdomain
        else:
            request.subdomain = None

        response = self.get_response(request)
        return response