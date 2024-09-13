from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("sort", include("sort.urls")),
]

# admin side custom
admin.site.site_title = "CAFE WEB"
admin.site.site_header = "CAFE WEB ADMINISTRATION"
admin.site.index_title = "CAFE WEB admin side"