from bitcast.settings.base import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()
# from django.contrib.auth.forms import SignupForm
# Create your views here.
from .forms import (
    AuthForm,
    SignupForm,

)


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect(settings.LOGIN_URL)
    else:
        print("리다렉트")
    return  render(request, 'accounts/signup_form.html', {
        'form': form,
        })


def profile(request):
    return render(request,'accounts/profile.html',{

        })