from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponse("Yes Hello world")
    else:
        return HttpResponse("No Hello World")