from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tattoo.models import TattooImage, Tattoo
from tattoo.models import Studio, TattooStudio
from tattoo.models import Deal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TattooImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooImage
        fields = ('id', 'name', 'owner', 'datafile')


class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = ('id', 'colored', 'style', 'temporary', 'place', 'image')


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'name', 'rating', 'location')


class TattooStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooStudio
        fields = ('id', 'price', 'tattoo', 'studio')


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('id', 'date', 'user', 'state', 'tatto_studio')

# admin.autodiscover()
