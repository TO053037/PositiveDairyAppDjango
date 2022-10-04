from django.db import models
from django.contrib.auth import get_user_model


class DairyContent(models.Model):
    content = models.TextField(
        max_length=300, verbose_name='楽しかったことを記入しよう', null=True, blank=True)
    date = models.DateField(null=False, blank=True)
    ranking = models.IntegerField(null=False, blank=True)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="dairyContent")


class PictureCategory(models.Model):
    title = models.CharField(max_length=60, verbose_name='カテゴリーのタイトル')
    comment = models.TextField(null=True, blank=True, max_length='200')
    picture_count = models.IntegerField(default=0)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="pictureCategory", blank=True, null=False)


class DairyPicture(models.Model):
    title = models.CharField(max_length=60, verbose_name='写真のタイトル')
    date = models.DateField(null=False, blank=True)
    image = models.ImageField(upload_to='images')
    comment = models.TextField(null=True, blank=True)
    category = models.ForeignKey(PictureCategory, on_delete=models.SET_NULL, related_name="dairyPicture", null=True)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="dairyPicture")
