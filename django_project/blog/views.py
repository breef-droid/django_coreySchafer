from django.shortcuts import render

POSTS_LIST = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    
]

def home(request):
    '''
    Function to handle traffic from homepage of blog
    '''
    context = {
        'posts': POSTS_LIST
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
