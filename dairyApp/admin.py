from django.contrib import admin
from .models import DairyContent, PictureCategory


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user_object', 'content', 'ranking', 'date')


admin.site.register(DairyContent, AuthorAdmin)


class PictureCategoryAdmin(admin.ModelAdmin):
    list_display = ('user_object', 'title', 'comment', 'picture_count')


admin.site.register(PictureCategory, PictureCategoryAdmin)
