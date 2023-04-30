import uuid

from django.db import models

class Artist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
        verbose_name="Name"
    )
    # albums: [0],
    # singles: [0, 1, 3, 5]

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
    #
    def __str__(self):
        return self.name