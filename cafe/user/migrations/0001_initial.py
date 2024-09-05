# Generated by Django 4.2.5 on 2024-09-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("username", models.SlugField(max_length=255, unique=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "prof_picture",
                    models.ImageField(
                        default="users/اصغر.jpg", upload_to="users/prof_%Y"
                    ),
                ),
                ("bio", models.TextField(blank=True, max_length=500)),
                ("phone_num", models.CharField(max_length=15, unique=True)),
                ("birthdate", models.DateField(blank=True, null=True)),
                ("pub_email", models.EmailField(blank=True, max_length=255)),
                ("tel_id", models.CharField(blank=True, max_length=50)),
                ("github_id", models.CharField(blank=True, max_length=50)),
                ("twitt_id", models.CharField(blank=True, max_length=50)),
                ("Youtube_id", models.CharField(blank=True, max_length=50)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]