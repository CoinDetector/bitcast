from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.





class Keyword(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )


    def __str__(self):
        return self.title



class Info(models.Model):
    detected_at =  models.DateTimeField(auto_now_add=True, verbose_name='긁어온 시간')
    info_count = models.PositiveIntegerField(default=0)
    #Keyword : Info = 1 : N
    keyword = models.ForeignKey(
        Keyword,
        on_delete=models.CASCADE,
    )