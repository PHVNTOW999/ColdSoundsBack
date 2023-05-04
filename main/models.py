import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

class Artist(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )
    
    avatar = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Avatar"
    )

    class Meta:
        verbose_name='Artist'
        verbose_name_plural='Artists'

    def __str__(self):
        return self.name

class Album(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    artists = models.ManyToManyField(
        Artist,
        null=False,
        blank=False,
        verbose_name="Artists",
        related_name="album_artists"
    )

    feat = models.ManyToManyField(
        Artist,
        null=True,
        blank=True,
        verbose_name="Featuring Artists"
    )
    
    cover = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Cover"
    )

    date = models.DateField()

    class Meta:
        verbose_name='Album'
        verbose_name_plural='Albums'

    def __str__(self):
        return self.name


class Single(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    file = models.FileField(
        validators=[FileExtensionValidator(['mp3', 'wav'])],
        upload_to='audio',
        verbose_name='Single File'
    )

    artists = models.ManyToManyField(
        Artist,
        null=False,
        blank=False,
        verbose_name="Artists",
        related_name="single_artists"
    )

    feat = models.ManyToManyField(
        Artist,
        null=True,
        blank=True,
        verbose_name="Featuring Artists"
    )

    cover = models.ImageField(
        validators=[FileExtensionValidator(['png', 'jpg'])],
        upload_to='img',
        blank=True,
        verbose_name='Single Cover',
    )

    date = models.DateField()

    class Meta:
        verbose_name = 'Single'
        verbose_name_plural = 'Singles'

    def __str__(self):
        return self.name