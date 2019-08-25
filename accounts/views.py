from django.shortcuts import render, redirect, reverse 
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

def index(request):
    """Return the index.html file """
    return render(request, "index.html")

def login(request):
    """Allow user to login"""
    if ['POST method']:
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have logged out, make sure you come back!")
    return redirect(reverse('home'))
