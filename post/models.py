# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    headline = models.CharField(max_length=100)
    content = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.CharField(max_length=50, default='none')
    published = models.BooleanField(default=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):              # __unicode__ on Python 2
        return self.name



class Comment(models.Model):
    text = models.TextField(max_length=50)
    comment_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.text
