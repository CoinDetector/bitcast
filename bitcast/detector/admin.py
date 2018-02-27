from django.contrib import admin
from .models import Keyword
from.models import Info





@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'title']
    list_diplay_links = ['title']

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'detected_at','info_count']

