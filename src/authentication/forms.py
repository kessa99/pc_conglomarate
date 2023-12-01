from django import forms
from .models import CustomUser

USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]

class SignUpForm(forms.ModelForm):

    username  = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none  focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Votre Username'
        })
    )

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none  focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Votre nom'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none  focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Votre nom'
        })
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none  focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Votre email'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Entrez votre mot de passe'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Confirmez votre mot de passe'
        })
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            'user_type',
        ]

class LoginForm(forms.Form):
    username  = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none  focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Votre Username'
        })
    )
   
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border p-2 w-full rounded focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Confirmez votre mot de passe'
        })
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1']