# Generated by Django 4.2.5 on 2024-09-05 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sort", "0001_initial"),
        ("blog", "0002_alter_article_open_conv"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ManyToManyField(blank=True, to="sort.category"),
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(blank=True, to="sort.tag"),
        ),
        migrations.CreateModel(
            name="BlogComment",
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
                ("email", models.EmailField(max_length=200)),
                ("full_name", models.CharField(max_length=200)),
                ("message", models.TextField(max_length=500)),
                ("show", models.BooleanField(default=False)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.article",
                    ),
                ),
            ],
        ),
    ]
