from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_dairy_content', views.post_dairy_content,
         name='post_dairy_content')
]
