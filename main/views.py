import json

from django.contrib.auth import get_user_model, login
from django.http import JsonResponse
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

            login(request, user)

            return JsonResponse(payload)


# main

class ArtistView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Artist.objects.get(uuid=self.kwargs['uuid'])
        serializer_class = ArtistSerializer(queryset)

        return JsonResponse(serializer_class.data)


class UserPlaylistView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Playlist.objects.filter(user__username=self.kwargs['email'])
        serializer_class = PlaylistSerializer(queryset, many=True, context={'request': request})

        return JsonResponse(serializer_class.data, safe=False)


class UserPlaylistUpdate(generics.UpdateAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Playlist.objects.get(uuid=self.kwargs['uuid'])
        serializer_class = PlaylistSerializer(queryset)

        return JsonResponse(serializer_class.data, safe=False)

    def patch(self, request, *args, **kwargs):
        queryset = Playlist.objects.get(uuid=self.kwargs['uuid'])

        if request.data['name']:
            queryset.name = request.data['name']

        if request.data['cover']:
            queryset.cover = request.data['cover']

        if request.data['date']:
            queryset.date = request.data['date']

        if request.data['files']:
            new_list = []

            for el in request.data['files']:
                new_list.append(Single.objects.get(uuid=el['uuid']))

            queryset.files.set(new_list)

        queryset.save()

        serializer_class = PlaylistSerializer(queryset)

        return JsonResponse(serializer_class.data, safe=False)


# View

class ArtistsListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SingleView(generics.ListAPIView):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer


class AllPlaylistsView(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
