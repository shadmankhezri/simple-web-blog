from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70 , unique_for_date='pub_date')
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now())
    slug = models.SlugField(null=True , blank=True , unique=True)




    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article , self).save()


    def get_absolute_url(self):
        return reverse('blog:article_detail' , kwargs={'slug':self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comments')

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='replies')

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]