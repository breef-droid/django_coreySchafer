from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm() #creates user form
    return render(request, 'users/register.html', {'form': form}) # renders html useing our form as an attribute