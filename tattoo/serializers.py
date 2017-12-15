from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tattoo.models import Tattoo
from tattoo.models import Studio
from tattoo.models import Deal


class UserSerializer(serializers.ModelSerializer):
    tattoos = serializers.PrimaryKeyRelatedField(many=True, queryset=Tattoo.objects.all())

    class Meta:
        model = User
        fields = ('username', 'email', 'tattoos')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class TattooImageSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = TattooImage
#         read_only_fields = ('id', 'name', 'owner', 'datafile')


# class PostViewSet(viewsets.ModelViewSet):
#     class Meta:
#         queryset = Post.objects.all()
#         serializer_class = PostSerializer
#         permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class TattooSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Tattoo
        fields = ('id', 'name', 'owner', 'style', 'image_file')


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'name', 'rating', 'lat', 'lng')


class DealSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    image = serializers.ReadOnlyField(source='tattoo.image_file.url')
    # studio = serializers.ReadOnlyField(source='studio.id')

    class Meta:
        model = Deal
        fields = ('id', 'date', 'user', 'state', 'price', 'tattoo', 'studio', 'colored', 'temporary', 'place', 'deal_code', 'image')

# admin.autodiscover()
