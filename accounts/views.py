from django.shortcuts import render, redirect, reverse 
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    """Return the index.html file, which is the registration landing page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if ['POST method']:
        registration_form = UserRegistrationForm(request.POST)
    
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account, please check all details and criteria match")
    else:
        registration_form = UserRegistrationForm()


    registration_form = UserRegistrationForm()
    return render(request, "index.html", {'registration_form': registration_form})


def login(request):
    """Allow user to login"""

    """Redirect user if they are aleady logged in"""               
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if ['POST method']:
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have logged out, make sure you come back!")
    return redirect(reverse('home'))

def profile(request):
    """ Profile page of user """
    user = User.objects.get(email=request.user.email)
    return render(request,'profile.html', {"profile": user})