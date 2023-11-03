from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .foorms import SignUpForm, AddRecordForm

# Create your views here.

# we will edit the home view after creating the model Record so we can see
# the Record on the site, we will also need to play with home.html

from .models import Record 

def home(request):
    # first we will create a variable to store all the Records:
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'successful registration')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form}) 
    return render(request, 'register.html', {'form': form})
            # we give the render some context with {'form': form}
            # we will now head back to register.html and do some things 
    # we will create register.html and it will extend base.html like the other HTML files

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    # we will use the c_r variable created here in record.html
    else:
        messages.success(request, 'you are not logged in')
        return redirect('home')

    # now we need to create a record.html page in templates 

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete a record')
        return redirect('home')

def add_record(request):
    # pass 
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added') 
                return redirect('home') 
        return render(request, 'add_record.html', {'form': form})  
    else:
        messages.success(request, 'You must be logged in to create a new record')
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        # we give the above an instance to populate the fields with 
        # the current record instead of the placeholders
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update a record')
        return redirect('home')

