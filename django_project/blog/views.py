from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    '''
    Function to handle traffic from homepage of blog
    '''
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    '''
    Function for about page landing
    '''
    return HttpResponse('<h1>Blog About</h1>')
