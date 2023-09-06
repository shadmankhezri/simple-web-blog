from django.shortcuts import render , redirect
from blog.models import Article
from django.urls import reverse

# Create your views here.

def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request , "home/index.html" , {'articles':articles })


def sidebar(request):
    data = {'name':'shadman'}
    return render(request , 'includes/sidebar.html' , context=data)