# Generated by Django 4.2.7 on 2023-12-14 04:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registerApp", "0002_favorites_readlist_delete_book"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Favorites",
            new_name="Favourites",
        ),
    ]
