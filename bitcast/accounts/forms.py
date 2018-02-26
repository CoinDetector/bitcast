from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "아이디 또는 패스워드가 틀렸습니다.",
        'inactive': "탈퇴한 계정입니다.",
    }

class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=32, help_text='username')
    phone_number = forms.CharField(max_length=32, help_text='phone_number')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
        )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(),
        help_text="Enter the same password as above, for verification."
         )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1','password2','phone_number']





