import uuid
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import CASCADE


class AudioFile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    format = models.CharField(
        default="audio",
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Format"
    )

    file = models.FileField(
        null=False,
        blank=False,
        validators=[FileExtensionValidator(['mp3', 'wav'])],
        upload_to='audio',
        verbose_name='Audio File'
    )

    class Meta:
        verbose_name = 'Audio File'
        verbose_name_plural = 'Audio Files'

    def __str__(self):
        return self.format


class ImgFile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    format = models.CharField(
        default="img",
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Format"
    )

    file = models.ImageField(
        null=False,
        blank=False,
        validators=[FileExtensionValidator(['jpg', 'png'])],
        upload_to='img',
        verbose_name='Image File'
    )

    class Meta:
        verbose_name = 'Image File'
        verbose_name_plural = 'Image Files'

    def __str__(self):
        return self.format


class Artist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    avatar = models.ForeignKey(
        ImgFile,
        null=True,
        blank=True,
        unique=False,
        on_delete=CASCADE
    )

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Single(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    cover = models.ForeignKey(
        ImgFile,
        null=False,
        blank=False,
        unique=False,
        on_delete=CASCADE
    )

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
        related_name="single_artists"
    )

    feats = models.ManyToManyField(
        Artist,
        null=True,
        blank=True,
        verbose_name="Featuring Artists"
    )

    files = models.FileField(
        null=False,
        blank=False,
        validators=[FileExtensionValidator(['mp3', 'wav'])],
        upload_to='audio',
        verbose_name='Audio File'
    )

    date = models.DateField(
        null=True,
        blank=True,
    )

    album = models.ForeignKey(
        to='main.Album',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Album (optional)",
    )

    position = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Position in album (optional)"
    )

    # duration = models.FloatField(
    #     blank=True,
    #     null=True,
    #     verbose_name="Audio duration"
    # )

    class Meta:
        verbose_name = 'Single'
        verbose_name_plural = 'Singles'
        ordering = ['position']

    def __str__(self):
        return self.name


class Album(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    cover = models.ForeignKey(
        ImgFile,
        null=False,
        blank=False,
        unique=False,
        on_delete=CASCADE
    )

    artists = models.ManyToManyField(
        Artist,
        null=False,
        blank=False,
        verbose_name="Artists",
        related_name="album_artists"
    )

    feats = models.ManyToManyField(
        Artist,
        null=True,
        blank=True,
        verbose_name="Featuring Artists"
    )

    files = models.ManyToManyField(
        Single,
        null=False,
        blank=False,
        verbose_name="Singles",
        related_name="album_single",
    )

    date = models.DateField()

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name


class Playlist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        unique=False,
        on_delete=CASCADE
    )

    cover = models.ForeignKey(
        ImgFile,
        null=False,
        blank=False,
        unique=False,
        on_delete=CASCADE
    )

    files = models.ManyToManyField(
        Single,
        null=False,
        blank=False,
        verbose_name="Singles",
        related_name="playlist_singles",
    )

    date = models.DateField()

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.name
