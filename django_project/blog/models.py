from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # allows us to use the User values as table

# Post model for storing posts in a db
class Post(models.Model):
    # each class is its own table in the db
    # each file will be an attribute in the table
    title = models.CharField(max_length= 100) # title character field with max length of 100
    content = models.TextField() # unrestricted text field
    date_posted = models.DateTimeField(default= timezone.now) #timezone in which the post was initially created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # grabs user table and handles when a user is deleted and what happens to the user posts

    # double underscore(dunder/magic methods)
    def __str__(self):
        return self.title