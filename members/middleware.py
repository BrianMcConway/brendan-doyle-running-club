from django.db import close_old_connections

class CloseDBConnectionsMiddleware:
    """
    Middleware to close old database connections after each request.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        close_old_connections()
        return response
