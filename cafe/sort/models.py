from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name