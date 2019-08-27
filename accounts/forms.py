from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 

class UserLoginForm(forms.Form):
    """ form to be used to log users in """
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

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    """ Form validation """
    def clean_email(self):
        """ Make sure user provides email address that is unique, and provides a username """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique")
        return email 
    
    def clean_password2(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        """ if password field has been left empty """
        if not password1 or not password2:
            raise ValidationError("Please confirm password")
        
        """ if both passwords don't match """
        if password1 != password2:
            raise ValidationError("Both passwords must match")
        
        return password2
