from django.contrib import admin
from . import models


@admin.register(models.Artist)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )
