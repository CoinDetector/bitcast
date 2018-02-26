from django.contrib import admin
from .models import Keyword






@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'title']
    list_diplay_links = ['title']
