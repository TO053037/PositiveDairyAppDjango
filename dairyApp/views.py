from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import DairyContent
import datetime
import json


def create_date_obj(date: str) -> datetime:
    return datetime.datetime.strptime(date, '%Y-%m-%d').date()


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
        dairy_content = {
            'content': request.POST.get('content'),
            'date': request.POST.get('date'),
            'ranking': request.POST.get('ranking'),
        }

        try:
            dairy_content_obj = DairyContent.objects.get(user_object=request.user,
                                                         date=create_date_obj(dairy_content['date']),
                                                         ranking=dairy_content['ranking'], )
            dairy_content_obj.content = dairy_content['content']
            dairy_content_obj.save()
        except DairyContent.DoesNotExist:
            DairyContent.objects.create(user_object=request.user, date=create_date_obj(dairy_content['date']),
                                        ranking=dairy_content['ranking'], content=dairy_content['content'])
        return JsonResponse({
            'dairyContent': dairy_content
        })
    raise Http404('not working')


@login_required
def get_dairy_content(request: HttpRequest):
    if request.method == 'GET':
        date = request.GET.get('date')
        ranking = request.GET.get('ranking')
        try:
            content = DairyContent.objects.get(user_object=request.user, ranking=ranking,
                                               date=datetime.datetime.strptime(request.GET.get('date'),
                                                                               '%Y-%m-%d').date()).content
            return JsonResponse({
                'status': 200,
                'content': content
            })
        except DairyContent.DoesNotExist:
            return JsonResponse({
                'status': 404,
            })
    raise Http404('not working')
