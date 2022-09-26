from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponse("Yes Hello world")
    else:
        return HttpResponse("No Hello World")