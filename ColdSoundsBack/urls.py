"""
URL configuration for ColdSoundsBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/http://127.0.0.1:8000/api/update-playlist/1cf978a6-f572-4dd5-b37f-05c3ca388b5e/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ColdSoundsBack import settings
from main.views import *

urlpatterns = [
    # auth
    path('admin/', admin.site.urls),
    path('api/auth/log/', LoginView.as_view(), name='login'),
    path('api/auth/reg/', RegView.as_view(), name='reg'),
    # main
    path('api/artists/', ArtistsListView.as_view(), name='artists_list'),
    path('api/artist/<uuid:uuid>/', ArtistView.as_view(), name='artist'),
    path('api/albums/', AlbumView.as_view(), name='albums_list'),
    path('api/singles/', SingleView.as_view(), name='singles_list'),
    path('api/playlists/', AllPlaylistsView.as_view(), name='playlists_list'),
    path('api/user-playlist/<str:email>/', UserPlaylistView.as_view(), name='user_playlist_list'),
    path('api/update-playlist/<uuid:uuid>/', UserPlaylistUpdate.as_view(), name='edit_user_playlist'),
    #files
    path('api/img-files/', UploadImgFileView.as_view(), name='artists_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
