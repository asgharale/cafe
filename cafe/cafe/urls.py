from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("user/", include("user.urls")),
    path("sort", include("sort.urls")),
]
