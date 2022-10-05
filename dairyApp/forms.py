from django import forms
from .models import PictureCategory, DairyPicture


class CategoryForm(forms.ModelForm):
    class Meta:
        model = PictureCategory
        fields = ['title', 'comment']


# class PictureForm(forms.ModelForm):
#     class Meta:
#         model = DairyPicture
#         fields = ['title', 'comment', 'image']


class PictureForm(forms.Form):
    title = forms.CharField(max_length=60)
    comment = forms.CharField(max_length=200)
    image = forms.FileField()
