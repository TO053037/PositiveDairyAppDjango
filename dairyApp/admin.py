from django.contrib import admin
from .models import DairyContent


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user_object', 'content', 'ranking', 'date')


admin.site.register(DairyContent, AuthorAdmin)
