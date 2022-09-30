from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import DairyContent
import datetime
import json


# Create your views here.

@login_required
def index(request: HttpRequest):
    print(request.user.email)
    context = {}
    return render(request, 'dairyApp/index.html', context)


@login_required
def post_dairy_content(request: HttpRequest):
    if request.method == 'POST':
        dairy_content = {
            'content': request.POST.get('content'),
            'date': request.POST.get('date'),
            'ranking': request.POST.get('ranking'),
        }
        DairyContent.objects.create(content=dairy_content['content'], user_object=request.user,
                                    ranking=dairy_content['ranking'],
                                    date=dairy_content['date'])
        return HttpResponse(json.dumps(dairy_content), content_type="application/json")
    raise Http404('not working')


@login_required
def get_dairy_content(request: HttpRequest):
    if request.method == 'GET':
        date = request.GET.get('date')
        ranking = request.GET.get('ranking')
        content = DairyContent.objects.get(user_object=request.user, ranking=ranking, date=date)
        return HttpResponse(json.dumps(content), content_type="applications/json")
    raise Http404('not working')
