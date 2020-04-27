from django.shortcuts import render, redirect, reverse 
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UpdateProfileForm
from to_do.models import Feature, Item
from checkout.models import Order
from accounts.models import UserProfile

def index(request):
    """Return the index.html file, which is the registration landing page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if ['POST method']:
        registration_form = UserRegistrationForm(request.POST or None)
    
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                password=request.POST['password1'],
                                first_name=request.POST['first_name'],
                                last_name=request.POST['last_name']
                                )

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account, please check all details and criteria match")
    else:
        registration_form = UserRegistrationForm()

    return render(request, "index.html", {'registration_form': registration_form})


def login(request):
    """Allow user to login"""

    """Redirect user if they are aleady logged in"""               
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if ['POST method']:
        login_form = UserLoginForm(request.POST or None)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Hi there " + str(user).capitalize() + "," + " you've successfully logged in")
                
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
    messages.success(request, "You've logged out, hopefully we'll see you again soon!")
    return redirect(reverse('home'))

def profile(request):
    """ Profile page of user """

    # Get user 
    user = User.objects.get(email=request.user.email)

    # Get orders, and filter them by the ones made by the user logged in. 
    # Displayed with the most recent at the top, and limited to 5 results 
    user_orders = Order.objects.filter(user=user).order_by("-date")[:5]

    # Get the features that have been liked by the user
    # Query results are limited to 8.
    user_liked_feature = Feature.objects.filter(likes=user)[:8]

    # Get the issues that have been liked by the user
    # Query results are limited to 8.
    user_liked_issues = Item.objects.filter(likes=user) [:8]

    return render(request, 'profile.html', {
        "profile": user, 
        "user_orders": user_orders,
        "user_liked_feature": user_liked_feature,
        "user_liked_issues": user_liked_issues})

def edit_profile(request):
    """ Function to edit the user profile - only favourite games is available at 
    the moment """
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated.")
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {
        "form": form, 
        "messages": messages
    })
