from rest_framework import serializers
from .models import *
import mutagen


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
    def some_pre_save_receiver(sender, instance):
        audio_info = mutagen.File(instance.files).info
        return audio_info

    test1 = serializers.CharField(default=some_pre_save_receiver)

    format = serializers.CharField(default='Single')

    class Meta:
        model = Single
        depth = 1
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    format = serializers.CharField(default='Playlist')

    class Meta:
        model = Playlist
        depth = 1
        fields = "__all__"
