from django.shortcuts import render , redirect
from blog.models import Article
from django.urls import reverse

# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request , "home/index.html" , {'articles':articles})