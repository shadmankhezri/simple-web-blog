from django.contrib.auth.models import User
from django.shortcuts import render , get_object_or_404 , redirect , HttpResponse
from blog.models import Article , Category , Comment , Message
from django.core.paginator import Paginator
from .forms import ContactUsForm , MessageForm
from django.views.generic.base import View , TemplateView
from django.views.generic import ListView
# Create your views here.

def post_detail(request , slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body , article=article , user=request.user , parent_id=parent_id)

    return render(request, "blog/article_detail.html", {"article":article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles , 2)
    objects_list = paginator.get_page(page_number)
    return render(request , "blog/articles_list.html" , {'articles':objects_list})


def category_detail(request , pk=None):
    category = get_object_or_404(Category , id=pk)
    articles = category.article_set.all()
    return render(request , "blog/articles_list.html" , {'articles':articles})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles , 2)
    objects_list = paginator.get_page(page_number)
    return render(request , "blog/articles_list.html" , {"articles":objects_list})


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request , "blog/contact_us.html" , {'form':form})





class Articlelist(TemplateView):
    template_name = "blog/article_list2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Article.objects.all()
        return context


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"






