from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to="store/products/%Y-%m", max_length=500)
    images = models.ManyToManyField("mediastore.Image")
    video = models.ManyToManyField("mediastore.Video")
    
    def __str__(self):
        return self.address + ' - ' + self.name