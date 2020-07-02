from django.db import models
from django import forms

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name


class Books(models.Model):
    coverpicture = models.URLField(max_length=255, null= True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField(null= True, blank= True)
    created = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='book_cat')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Books,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



