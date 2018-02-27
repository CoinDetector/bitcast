from django import forms
from .models import Keyword



class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ['title']