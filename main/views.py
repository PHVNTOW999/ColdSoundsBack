import datetime

from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *
from .models import *


# auth

class RegView(APIView):
    def post(self, request):
        if User.objects.filter(email=request.data['email']):
            raise AuthenticationFailed('This email has already been registered!')

        if request.data['password'] != request.data['password2']:
            raise AuthenticationFailed('Password mismatch!')

        else:

            user = User.objects.create_user(
                email=request.data['email'],
                username=request.data['email'],
                password=request.data['password']
            )

            user.save()

            return Response(f"Registration is done! Your welcome - {user.email}")


class LoginView(APIView):
    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = get_user_model().objects.filter(email=email).first()

        if email is None:
            raise AuthenticationFailed('Email not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        else:

            payload = {
                "id": user.id,
                "email": user.email,
                "is_admin": user.is_staff,
                "last_login": user.last_login,
                "reg_date": user.date_joined.strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse(payload)


# main

class ArtistView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SingleView(generics.ListAPIView):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer
