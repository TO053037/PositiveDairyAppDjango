from django import forms
from .models import PictureCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = PictureCategory
        fields = ['title', 'comment']

        