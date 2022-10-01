from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import DairyContent
import datetime
import json


# Create your views here.

@login_required
def index(request: HttpRequest):
    print(request.user.email)
    context = {
        'today': datetime.date.today().strftime("%Y-%m-%d"),
    }
    print(context)
    return render(request, 'dairyApp/index.html', context)


@login_required
def post_dairy_content(request: HttpRequest):
    if request.method == 'POST':
        date_object = datetime.datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
        print(date_object)
        dairy_content = {
            'content': request.POST.get('content'),
            'date': request.POST.get('date'),
            'ranking': request.POST.get('ranking'),
        }

        print(dairy_content['date'])
        DairyContent.objects.create(content=dairy_content['content'], user_object=request.user,
                                    ranking=dairy_content['ranking'],
                                    date=datetime.datetime.strptime(dairy_content['date'], '%Y-%m-%d').date())
        return JsonResponse({
            'dairyContent': dairy_content
        }
        )
    raise Http404('not working')


@login_required
def get_dairy_content(request: HttpRequest):
    if request.method == 'GET':
        date = request.GET.get('date')
        print(date)
        ranking = request.GET.get('ranking')
        content = DairyContent.objects.get(user_object=request.user, ranking=ranking,
                                           date=datetime.datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date()).content
        print(content)
        return JsonResponse({
            'content': content
        })
    raise Http404('not working')
