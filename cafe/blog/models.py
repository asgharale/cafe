from django.db import models
from django.conf import settings

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
    category = models.ManyToManyField("sort.Category", blank=True)
    tags = models.ManyToManyField("sort.Tag", blank=True)
    # body(reach text editor), some ai features
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES)
    read_time = models.SmallIntegerField()
    views = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="viewed")
    created_at = models.DateField()
    last_modified = models.DateField(auto_now=True)
    open_conv = models.BooleanField(default=True, verbose_name="Open Converstaion")    

    def __str__(self):
        return self.title + " - " + self.address

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def likes_count(self):
        return self.views.count()

    class Meta:
        ordering = ('last_modified',)



class BlogComment(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField(max_length=200)
    full_name = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    show = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.article.title} - {self.full_name} - {self.email}"