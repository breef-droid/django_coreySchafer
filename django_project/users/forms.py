from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    '''
        Fine tunes the user registration form, inherits from the UserCreationForm class
    '''
    email = forms.EmailField() # required = true by default

    class Meta:
        '''
        Sub-class which tells django which model to save new users to
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # fields we want in our form