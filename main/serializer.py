from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        depth = 1
        fields = "__all__"