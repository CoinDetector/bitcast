from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
admin.site.register(User)
# Register your models here.
