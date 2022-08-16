from django.shortcuts import render
from .models import Post # . refers to model package i

def home(request):
    '''
    Function to handle traffic from homepage of blog
    '''
    context = {
        'posts': Post.objects.all() # accesses the posts in the current db
    }
    return render(request, 'blog/home.html', context)

def about(request):
    '''
    Function for about page landing
    '''
    context = {
        'title' : 'About Jou Ma'
    }
    return render(request, 'blog/about.html', context)
