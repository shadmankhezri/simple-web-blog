from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
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


    def __str__(self):
        return f"{self.title} - {self.body[:30]}"