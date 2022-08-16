from django.contrib import admin
from .models import Post

# Register our models to enable a view on admin page
admin.site.register(Post)