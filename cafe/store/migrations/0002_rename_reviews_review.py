# Generated by Django 4.2.5 on 2024-09-06 19:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="reviews",
            new_name="Review",
        ),
    ]
