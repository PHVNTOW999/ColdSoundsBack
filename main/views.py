from rest_framework import generics
from .serializer import *
from .models import *

class ArtistView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SingleView(generics.ListAPIView):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer
