from django.shortcuts import render, redirect
from django.contrib import messages # used for sending flash messages to client
from .forms import UserRegisterForm


def register(request):
    #logic to handle what to do with POST requests from new users
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # logic to handle if form is valid
        if form.is_valid():
            form.save() # saves user hashes password
            username = form.cleaned_data.get('username') # init the username from valid forms
            messages.success(request, f'Account created for {username}!') # shows success message
            return redirect('blog-home') # redirects user on succesfull registration to blog-home page
    else:
        form = UserRegisterForm()#creates user form

    return render(request, 'users/register.html', {'form': form}) # renders html useing our form as an attribute

# messages.debug(request, message)
# messages.info(request, message)
# messages.success(request, message)
# messages.warning(request, message)
# messages.error(request, message)