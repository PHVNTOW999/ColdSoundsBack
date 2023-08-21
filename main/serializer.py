from django.forms import forms
from rest_framework import serializers
from .models import *


class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        depth = 1
        fields = "__all__"


class ImgFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgFile
        depth = 1
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        depth = 1
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    format = serializers.CharField(default='Album')

    class Meta:
        model = Album
        depth = 1
        fields = "__all__"


class SingleSerializer(serializers.ModelSerializer):
    format = serializers.CharField(default='Single')

    class Meta:
        model = Single
        depth = 1
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    files = SingleSerializer(many=True)
    format = serializers.CharField(default='Playlist')

    class Meta:
        model = Playlist
        depth = 1
        fields = "__all__"
