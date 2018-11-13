# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .models import Post, Category, Comment


def index(request):
    if request.user.is_authenticated():
        posts_list = Post.objects.all().order_by('-pub_date')
    else:
        posts_list = Post.objects.filter(published=True).order_by('-pub_date')
    cats = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/index.html', {'posts':posts, 'cats':cats, 'success':['user created successfully']})


def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    cats = Category.objects.all()
    comments = Comment.objects.filter(article=post)
    return render(request, 'post/post.html', {'post':post, 'comments':comments})


def edit_post(request, pk):
    my_user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        post = Post.objects.get(pk=pk)
        if post.user == my_user:
            post.headline = title
            post.content = body
            post.save()
        return redirect('/'+pk)
    post = Post.objects.get(id=pk)
    return render(request, 'post/edit_post.html', {'post':post})

def delete_post(request, pk):
    my_user = request.user
    post = Post.objects.get(id=pk)
    if post.user == my_user:
        post.delete()

    return redirect('/')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        #category = request.POST.get('category')

        post = Post(headline=title, content = body, user = request.user)#, cat = category)
        post.save()
        return redirect('/')
    return render(request, 'post/create_post.html', {})

def publish(request, pk):
    post = Post.objects.get(id=pk)
    if post.published:
        post.published = False
    else:
        post.published = True
    post.save()
    return redirect('/')

