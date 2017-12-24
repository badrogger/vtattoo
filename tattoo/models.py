import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geoip import GeoIP
from django.core.files.storage import FileSystemStorage
from vtattoo.settings import MEDIA_ROOT
from rest_framework import serializers


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class StudioManager(models.Manager):
    def new():
        pass

    def popular():
        pass


class TattooManager(models.Manager):
    def new():
        pass

    def popular():
        pass


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TATTOO_IMG_PATH = os.path.join(MEDIA_ROOT, "tattooimg")
tattoofs = FileSystemStorage(TATTOO_IMG_PATH)


class Studio(models.Model):
    objects = StudioManager()
    name = models.CharField(default="", max_length=255)
    rating = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    temporary_price = models.FloatField(default=-1)
    colored_price = models.FloatField(default=-1)
    temp_col_price = models.FloatField(default=-1)
    regular_price = models.FloatField(default=10)


class Tattoo(models.Model):
    objects = TattooManager()
    name = models.CharField(default="", max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    style = models.CharField(default="", max_length=255)
    public = models.BooleanField(default=True)
    image_file = models.ImageField(
        storage=tattoofs,
        default=os.path.join(TATTOO_IMG_PATH, "cup.jpg")
    )

    class Meta:
        ordering = ('created',)


class Deal(models.Model):
    date = models.DateTimeField(null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(default="in progress", max_length=255)
    price = models.FloatField(default=0.0)
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE, null=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True)
    deal_code = models.CharField(default="11111111111111111111", max_length=30)
    colored = models.BooleanField(default=False)
    temporary = models.BooleanField(default=False)
    place = models.TextField(default="shoulder")
