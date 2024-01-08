from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    print(articles)
    return render(request, 'site_back/index.html', {'articles': articles})