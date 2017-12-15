import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geoip import GeoIP
from django.core.files.storage import FileSystemStorage
from vtattoo.settings import MEDIA_ROOT
from rest_framework import serializers


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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
