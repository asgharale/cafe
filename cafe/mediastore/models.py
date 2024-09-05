from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    file = models.ImageField(upload_to="images/%Y-%m/")
    
    def __str__(self):
        return self.name + ' - ' + self.alt

class Video(models.Model):
    name = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    file = models.ImageField(upload_to="videos/%Y-%m/")
    
    def __str__(self):
        return self.name + ' - ' + self.alt

class File(models.Model):
    name = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    file = models.ImageField(upload_to="files/%Y-%m/")
    
    def __str__(self):
        return self.name + ' - ' + self.alt