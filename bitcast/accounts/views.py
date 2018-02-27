from bitcast.settings.base import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from detector.models import Keyword
from django.conf import settings
from django.contrib import auth
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
        print(Keyword.objects.filter(title="정부 규제").count())
        print("-----------------------------")
        if Keyword.objects.filter(title="정부 규제").count() != 0:
            keyword = Keyword.objects.filter(title='정부 규제')
            keyword.update()
            keyword[0].users.add(user.pk)



        else:
            print("자식아")
            sample = Keyword()
            sample.save()
            sample.users.add(user.pk)
            sample.title = '정부규제'


        return redirect(settings.LOGIN_URL)
    else:
        print("리다렉트")
    return  render(request, 'accounts/signup_form.html', {
        'form': form,
        })


def profile(request):
    return render(request,'accounts/profile.html',{

        })