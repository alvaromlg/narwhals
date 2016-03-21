from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from helpers import error_response

def api_key_checker(f):
    def wrapper(*args, **kwargs):
        for param in args:
            if isinstance(param, Request):
                request = param

        key_provided = request.GET.get('api_key', '')
        if key_provided != getattr(settings, 'API_KEY'):
            return Response(error_response("Api key needed."),
                            status=status.HTTP_400_BAD_REQUEST)
        return f(*args)
    return wrapper

