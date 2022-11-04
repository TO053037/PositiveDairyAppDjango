from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


class DairyContent(models.Model):
    content = models.TextField(
        max_length=300, verbose_name='楽しかったことを記入しよう', null=True, blank=True)
    date = models.DateField(null=False, blank=True)
    ranking = models.IntegerField(null=False, blank=True)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="dairyContent")

    def __str__(self):
        return self.content


class PictureCategory(models.Model):
    title = models.CharField(max_length=60, verbose_name='カテゴリーのタイトル')
    comment = models.TextField(null=True, blank=True, max_length='200')
    picture_count = models.IntegerField(default=0)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="pictureCategory", blank=True, null=False)

    def __str__(self):
        return self.title


class DairyPicture(models.Model):
    title = models.CharField(max_length=60, verbose_name='写真のタイトル')
    date = models.DateField(null=False, blank=True)
    # image = models.ImageField(upload_to='images')
    image = CloudinaryField(
        'image', folder="images/cloudinary")
    comment = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(PictureCategory, on_delete=models.SET_NULL, related_name="dairyPicture", null=True,
                                 default=None)
    user_object = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="dairyPicture")

    def __str__(self):
        return self.title
