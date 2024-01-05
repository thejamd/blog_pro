from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date,datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default='blog-site')
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank =True,null =True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add =True)
    category = models.CharField(max_length=255,default='coding')
    def __str__(self):
        return self.title + '|' + str(self.auther)
    def get_absolute_url(self):
        return reverse('article_detail',args=str(self.id))