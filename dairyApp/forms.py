from django import forms
from .models import DairyContent


class DairyContentForm(forms.ModelForm):
    class Meta:
        model = DairyContent
        fields = ['content']
        