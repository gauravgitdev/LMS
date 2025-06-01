from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Required. 30 characters or fewer.',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Required. 30 characters or fewer.',
            'class': 'form-control'
        })
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Required. 150 characters or fewer...',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Required. Inform a valid email address.',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Required. 8 characters or more.',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter the same password again.',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = None
        try:
            user= User.objects.get(email=email)
        except:
            return email
        
        if (user is not None):
            raise forms.ValidationError("Email already exists")
    
        # we can create clean functions for other fields as well when needed