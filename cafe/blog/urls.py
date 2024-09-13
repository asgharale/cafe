from django.urls import path
from .views import home, article_view

urlpatterns = [
	path("", home, name="blog_home"),
	path("articles/<slug:address>", article_view)
]