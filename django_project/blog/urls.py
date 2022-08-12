from django.urls import path
from . import views # . is used to import functions from other files

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]