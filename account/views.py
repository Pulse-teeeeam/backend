from rest_framework import generics, response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import serializers

class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is None:
                return response.Response(
                    {"detail": "Invalid credentials."},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            token, created = Token.objects.get_or_create(user=user)

            return response.Response(
                {"token": token.key},
                status=status.HTTP_200_OK
            )

        return response.Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
