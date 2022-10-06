from django import forms
from .models import PictureCategory, DairyPicture


class CategoryForm(forms.ModelForm):
    class Meta:
        model = PictureCategory
        fields = ['title', 'comment']


class DairyPictureForm(forms.ModelForm):
    class Meta:
        model = DairyPicture
        fields = ['title', 'comment', 'image', 'category']

    def __init__(self, user, *args, **kwargs):
        super(DairyPictureForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = PictureCategory.objects.filter(user_object=user)
        self.fields['category'].required = False

# class DairyPictureForm(forms.Form):
#     title = forms.CharField(max_length=60)
#     comment = forms.CharField(max_length=200)
#     image = forms.FileField()
