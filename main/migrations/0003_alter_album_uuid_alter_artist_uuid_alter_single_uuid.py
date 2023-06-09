# Generated by Django 4.2 on 2023-05-02 11:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_format_remove_artist_slug_id_artist_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b1470527-b575-45b1-82e2-69bc02eca4c3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('49f079ff-c778-4e03-a59d-19884eb0ceb4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='single',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9f756fd3-f4d5-4c7c-88a8-5fa547177ebd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
