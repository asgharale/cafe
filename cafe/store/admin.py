from django.contrib import admin
from store.models import Detail, DiscountGroup, Product, Review


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(DiscountGroup)
admin.site.register(Detail)

