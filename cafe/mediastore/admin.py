from django.contrib import admin
from mediastore.models import Image, Video, File


admin.site.register(Image)
admin.site.register(Video)
admin.site.register(File)