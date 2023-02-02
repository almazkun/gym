import logging

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserCreateSerializer

logger = logging.getLogger(__name__)


class UserCreateView(APIView):
    """### Create a new user in the system.

    Every request needs to have the Authorization token in the header:
    `"Authorization: Token bb56cbff98cf68bc741edd182e3ea42f81b5b360"`

    * #### Parameters:
    `username` - Username of the user.
    `password` - Password of the user.
    `email` - Email of the user.

    * #### Example:
    `curl -X POST -H 'Content-Type: application/json' -d '{"username": "test", "password": "test", "email": "email@email.com"}' http://localhost:8000/accounts/users/create/`

    * #### Response:
    `{"username":"test","email":"email@email.com"}`
    """

    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        logger.debug("UserCreateView.post")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ObtainAuthTokenView(APIView):
    """### Obtain an authentication token for a user.

    Every request needs to have the Authorization token in the header:
    `"Authorization: Token bb56cbff98cf68bc741edd182e3ea42f81b5b360"`

    * #### Parameters:
    `username` - Username of the user.
    `password` - Password of the user.

    * #### Example:
    `curl -X POST -H 'Content-Type: application/json' -d '{"username": "test", "password": "test"}' http://localhost:8000/accounts/token/`

    * #### Response:
    `{"token":"bb56cbff98cf68bc741edd182e3ea42f81b5b360"}`
    """

    serializer_class = AuthTokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        logger.debug("ObtainAuthTokenView.post")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
