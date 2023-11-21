from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Obligatoire entrez votre nom.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Obligatoire entrez votre prenom.')
    email = forms.EmailField(max_length=254, help_text='entrez un email valid')
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            'user_type',
        ]


# class SignUpForm(UserCreationForm):
#     user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password1', 'user_type']


# class SignInForm(UserCreationForm):
#     user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2', 'user_type']
