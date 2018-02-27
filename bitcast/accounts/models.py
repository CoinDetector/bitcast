from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    phone_number = models.CharField(max_length=20, blank=True)
