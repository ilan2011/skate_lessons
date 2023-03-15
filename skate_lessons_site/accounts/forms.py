from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from .models import CustomUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, required=True, help_text='Required')
    first_name = forms.CharField(
        max_length=255, required=True, help_text='Required')
    last_name = forms.CharField(
        max_length=255, required=True, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
