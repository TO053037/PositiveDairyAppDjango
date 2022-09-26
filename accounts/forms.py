from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
