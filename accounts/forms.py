from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class signUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2',
                  'email')
