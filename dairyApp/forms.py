from django import forms
from .models import PictureCategory, DairyPicture


class CategoryForm(forms.ModelForm):
    class Meta:
        model = PictureCategory
        fields = ['title', 'comment']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'border-2 border-black py-5 align-middle'
        self.fields['title'].widget.attrs['rows'] = 1
        self.fields['comment'].widget.attrs['class'] = 'border-2 border-black py-5 align-middle'


class DairyPictureForm(forms.ModelForm):
    class Meta:
        model = DairyPicture
        fields = ['title', 'comment', 'image', 'category']

    def __init__(self, *args, **kwargs):
        self.user_object = kwargs.pop('user_object')
        super(DairyPictureForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = PictureCategory.objects.filter(user_object=self.user_object)
        self.fields['category'].required = False
        self.fields['category'].widget.attrs['class'] = 'border-2 border-black py-3 align-middle'
        self.fields['title'].widget.attrs['class'] = 'border-2 border-black py-3 align-middle'
        self.fields['comment'].widget.attrs['class'] = 'border-2 border-black py-3 align-middle'

# class DairyPictureForm(forms.Form):
#     title = forms.CharField(max_length=60)
#     comment = forms.CharField(max_length=200)
#     image = forms.FileField()
