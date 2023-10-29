from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages  

# Create your views here.

def home(request):
    # check to see if logging in:
    if request.method == 'POST': # method='POST' is in home.html in form tag
        user_name = request.POST['user_name']
        pass_word = request.POST['pass_word']
        # user_name comes from the form tag in home.html (div input type text)
        # same with password
        # authenticate:
        user = authenticate(request, username=user_name, password=pass_word) # we can call user something else if we please
        # 3 params in authenticate
        if user is not None:
            login(request, user)
            messages.success(request, 'you are now free to fly about the website')
            return redirect('home')
        else:
            messages.success(request, 'loggin no good, you must stay grounded')
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    # to get messages going we need to add some code to base.html

def login_user(request):
    pass
    # we can add the code from home if we want to create a separate login page

def logout_user(request):
    # pass
    # much easier than than the login function
    logout(request)
    # would work without messages but we will add some anyway:
    messages.success(request, 'you have landed successfully and are logged out')
    return redirect('home')
    # we now need to add a link to this in the navbar, see the link we saved in the 
    # beginning, one thing we will do is change the # that points no where and another
    # thing is to change the text Link to Logout

def register_user(request):
    return render(request, 'register.html', {}) 
    # we will create register.html and it will extend base.html like the other HTML files
