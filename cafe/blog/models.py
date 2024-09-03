from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    meta = models.TextField(max_length=400)
    # tag, category, body, thumbnail, some ai features
    author = models.ForeignKey("user.CUser", on_delete=models.CASCADE)