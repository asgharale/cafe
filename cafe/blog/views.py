from django.shortcuts import render
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles
    }
    return render(request, "blog/main.html", context)

def article_view(request, address):
    pass