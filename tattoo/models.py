import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geoip import GeoIP
from django.core.files.storage import FileSystemStorage
from vtattoo.settings import MEDIA_ROOT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.


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
    location = GeoIP()


class TattooImage(models.Model):
    datafile = models.ImageField(
        storage=tattoofs,
        default=os.path.join(TATTOO_IMG_PATH, "cup.jpg")
    )
    name = models.CharField(default="", max_length=255)
    owner = models.ForeignKey(User, to_field='id')
    created = models.DateTimeField(auto_now_add=True)


class Tattoo(models.Model):
    objects = TattooManager()
    colored = models.BooleanField(default=False)
    style = models.CharField(default="", max_length=255)
    temporary = models.BooleanField(default=False)
    place = models.TextField(default="shoulder")
    image = models.OneToOneField(
        TattooImage,
        on_delete=models.CASCADE,
        null=True
    )


class TattooStudio(models.Model):
    price = models.IntegerField(default=0)
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)


class Deal(models.Model):
    date = models.DateTimeField(null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(default="in progress", max_length=255)
    tattoo_studio = models.ForeignKey(TattooStudio, on_delete=models.CASCADE)
