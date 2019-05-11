from django import forms
from .models import Lost

class Lost(forms.ModelForm):
    class Meta:
        model = Lostform
        fields = ['title', 'author', 'image', 'content', 'password']