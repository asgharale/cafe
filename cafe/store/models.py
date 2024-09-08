from django.db import models

class DiscountGroup(models.Model):
    title = models.CharField(unique=True, max_length=100)
    meta = models.TextField(max_length=400, blank=True)
    amount = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title + ' - ' + self.amount

class Detail(models.Model):
    title = models.CharField(max_length=255)
    value = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUSES = (
        ('T', "Published"),
        ('F', "Draft"),
    )

    title = models.CharField(max_length=255)
    address = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to="store/products/%Y-%m", max_length=500)
    meta = models.TextField(max_length=400)
    exist = models.BooleanField(default=False)
    images = models.ManyToManyField("mediastore.Image")
    videos = models.ManyToManyField("mediastore.Video")

    categories = models.ManyToManyField("sort.Category", blank=True)
    Tags = models.ManyToManyField("sort.Tag", blank=True)

    org_price = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=0)
    discount_group = models.ForeignKey(DiscountGroup, on_delete=models.DO_NOTHING, blank=True)
    buyers = models.IntegerField(default=0)

    details = models.ManyToManyField(Detail)
    # description (reachtext editor)

    status = models.CharField(max_length=1, choices=STATUSES, default='F')

    def __str__(self):
        return self.address + ' - ' + self.title
    def get_sell_price(self):
        min = self.org_price * ((100-self.discount)/100)
        if self.discount_group:
            group_price = self.org_price * ((100-self.discount_group.amount)/100)
            if min>group_price:
                min = group_price
        return min
    def get_score(self):
        pass

class Review(models.Model):
    user = models.OneToOneField("user.CUser", on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING, related_name="reviews")
    point = models.SmallIntegerField(default=0)
    comment = models.TextField(max_length=500)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username + ' -ON- ' + self.product.title


class Ad(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title