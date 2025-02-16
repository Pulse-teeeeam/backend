from rest_framework import generics, response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from . import serializers, api_elc, models
from django.contrib.auth import get_user_model

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

class ELCGenerate(APIView):
    def get(self, request):
        return HttpResponseRedirect(redirect_to=api_elc.client.generate_url())

class ELCLogin(APIView):
    def get(self, request):
        User = get_user_model()
        code = request.GET['code']
        try:
            elc_id = api_elc.client.auth(code)
        except:
            return response.Response('Error')

        try:
            user = User.objects.get(code_etc=elc_id)
        except User.DoesNotExist:
            user = User.objects.create(code_etc=elc_id, username=f'elc{elc_id}', is_active=False)

        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return HttpResponseRedirect(redirect_to=f'/panel/elc?token={token}')
        else:
            return HttpResponseRedirect(redirect_to='/panel/elc/wait_active')


