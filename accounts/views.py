from django import shortcuts
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import CustomUserCreationForm, LoginForm

from django.contrib.auth.views import LoginView


def signup(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email,
                                password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('index')
    else:
        form = CustomUserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login')
