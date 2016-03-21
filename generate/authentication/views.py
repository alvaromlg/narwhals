from rest_framework import parsers, renderers
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Django REST Authentication
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.helpers import success_response, error_response
from serializers import UserSerializer
from models import User
from utils.decorators import api_key_checker

class UserView(viewsets.ModelViewSet):
    """
    API endpoint for User
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer
    model = User


class ObtainAuthToken(APIView):
    """
    Overriding this Django REST class
    to also return the User.
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    @api_key_checker
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_serialized = UserSerializer(user)
            return Response(success_response(user_serialized.data))
        else:
            return Response(error_response("User or password incorrect."))

