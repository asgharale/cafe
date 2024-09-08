from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("sort", include("sort.urls")),
]
