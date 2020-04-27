from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 
from .models import UserProfile

class UserLoginForm(forms.Form):
    """ Form to be used to log users in """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """ Registration form to create a new user """

    password1 = forms.CharField(
                                widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(
                                label="Password Confirmation", 
                                widget=forms.PasswordInput)
    
    email = forms.EmailField(label="Email address")

    first_name = forms.CharField(max_length=50)

    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_email(self):
        """ Make sure user provides email address that is unique, and provides a username """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("This email address has already been used")
        return email 
    
    def clean_password2(self):
        """ Validate password - check it has a certain number of letters
        and passwords match when confirming """ 

        min_length = 8

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Check the password has the required length of letters
        if len(password1) < min_length:
            raise ValidationError(('Password needs to be {0} letters long').format(min_length))


        # Check password has been entered 
        if not password1 or not password2:
            raise ValidationError("Please confirm password")
        
        # Check passwords match when confirming password
        if password1 != password2:
            raise ValidationError("Both passwords must match")
            
        return password2

class UpdateProfileForm(forms.ModelForm):
    """ Form to be used to edit user profile - specifically the favourite 
    game section """

    favourite_games = forms.CharField(max_length=100)

    class Meta:
        model = UserProfile
        fields = ('favourite_games', )
