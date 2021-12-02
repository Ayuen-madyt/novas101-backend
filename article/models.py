from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.utils.html import escape
from django.utils import timesince #importinng timesince
import uuid

# Create your models here.   

# class Category(models.Model):
#     categoryName = models.CharField(max_length=150)

#     class Meta:
#         verbose_name_plural = 'Category'

#     def __str__(self):
       
#         return self.categoryName

class Article(models.Model):
    CATEGORIES = (
        ('NEWS', 'NEWS'),
        ('SPORTS', 'SPORTS'),
        ('POLITICS', 'POLITICS'),
        ('LIFESTYLE', 'LIFESTYLE'),
        ('FASHION', 'FASHION'),
        ('ENTERTAINMENT', 'ENTERTAINMENT'),
        ('BUSINESS', 'BUSINESS'),
        ('TECHNOLOGY', 'TECHONOLOGY'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, help_text="Title should not be more than 15 words")
    image = models.FileField(null=True, blank=True) 
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    category = models.CharField(choices=CATEGORIES, max_length=150)
    trending = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'articles'
        ordering = ['-date_added']

    @property
    def time_added(self):
        return timesince.timesince(self.date_added)

    def __str__(self):
        return self.title


class Views(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True,blank=True, related_name="views")
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Views'
    
    def __str__(self):
        return f'{self.article} ({self.views} views)'

    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=500)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.name} commented on {self.article.title}'
    




# class SubCategory(models.Model):
#     # post = models.ForeignKey(Article,on_delete=models.CASCADE, null=True, blank=True)
#     sub_category = models.CharField(max_length=150)

#     class Meta:
#         verbose_name_plural = 'sub-categories'

#     def __str__(self):
       
#         return self.sub_category