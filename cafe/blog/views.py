from django.shortcuts import render

def home(request):
    return render(request, "blog/main.html")

def article_view(request, address):
    pass