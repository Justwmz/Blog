from django.http.response import Http404
from django.shortcuts import render
from .models import *

# Create your views here.

def index (request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories' : categories
    }

    return render(request, 'blog/index.html', context=context)

def about (request):
    return render(request, 'blog/about.html')

def view_post(request, post_id):
    return render(request)

def view_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    categories = Category.objects.all()

    if len(posts) == 0:
        raise Http404()
    
    context = {
        'posts': posts,
        'categories' : categories
    }
    
    return render(request, 'blog/index.html', context=context)