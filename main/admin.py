from django.contrib import admin
from . import models


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )

@admin.register(models.Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )

@admin.register(models.Single)
class SingleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )