from django.db import models

class Article(models.Model):
    STATUSES = (
        ('T', "Published"),
        ('F', "Draft"),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    meta = models.TextField(max_length=400)
    thumbnail = models.ImageField(upload_to="blog/thumbnails_%Y/", blank=True, max_length=255)
    # tag, category, body(reach text editor), some ai features, comments 
    author = models.ForeignKey("user.CUser", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES)
    read_time = models.SmallIntegerField()
    views = models.IntegerField()
    likes = models.IntegerField()
    created_at = models.DateField()
    last_modified = models.DateField(auto_now=True)
    
    open_conv = models.BooleanField(default=True)