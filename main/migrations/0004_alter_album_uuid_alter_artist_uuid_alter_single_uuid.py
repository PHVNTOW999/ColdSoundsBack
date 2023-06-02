# Generated by Django 4.2 on 2023-05-02 12:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_album_uuid_alter_artist_uuid_alter_single_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1457aa74-7daa-4707-b85b-245de9b4496a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c2fe5baf-2fc3-45c5-a171-54aa04835b10'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='single',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('42a4db86-e757-42dd-ae82-6ed58128d52c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
