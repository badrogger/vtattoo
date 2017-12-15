# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from blog.forms import LoginForm, SignUpForm
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login, logout as auth_logout
import os
import PIL
import random
import string
import logging
from rest_framework import status
from django.contrib.auth.models import User, Group
from tattoo.models import Tattoo, Studio, Deal
from rest_framework import viewsets, permissions
from rest_framework import generics
from tattoo.serializers import UserSerializer, GroupSerializer
from tattoo.serializers import StudioSerializer, TattooSerializer, DealSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser
from django.views.generic import TemplateView
from django.http import HttpResponse
from vtattoo import settings
from django.core.files.storage import FileSystemStorage
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
# from oauth2_provider.contrib.rest_framework import TokenHasScope


logger = logging.getLogger(__name__)

logging.basicConfig(filename='views.log', level=logging.DEBUG)


def random_deal_code():
    return ''.join(random.randint(0, 9) for i in range(20))


# poor rest
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserSerializer(serializers.ModelSerializer):
#     # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')


# class TattooImageList(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, format=None):
#         tattoo_images = TattooImage.objects.all()
#         serializer = TattooImageSerializer(tattoo_images, many=True)
#         return Response(serializer.data)


# class TattooList(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, format=None):
#         tattoos = Tattoo.objects.all()
#         serializer = TattooSerializer(tattoos, many=True)
#         return Response(serializer.data)


class TattooIndexList(generics.ListAPIView):
    # queryset = Tattoo.objects.all()[:6]
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer


class UserTattooList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        # raise user.id
        all_list = Tattoo.objects.all()
        logging.info(all_list)
        logging.info([(t.name, t.owner) for t in all_list])
        return_list = list(filter(lambda x: x.owner == user, all_list))
        return return_list

    # queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer


class TattooCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

    def perform_create(self, serializer):
        # logging.info(self.request)
        t_file = self.request.data.get('file')
        # splitted = t_file.name.rsplit(".", 1)
        # code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        # t_file.name = ''.join((splitted[0], code, '.', splitted[1]))
        serializer.save(owner=self.request.user, image_file=t_file)


class TattooDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer


class StudioList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        studios = Studio.objects.all()
        serializer = StudioSerializer(studios, many=True)
        return Response(serializer.data)


class StudioCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class DealList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, deal_code=random_deal_code())

    def get_queryset(self):
        user = self.request.user
        # raise user.id
        all_list = Deal.objects.all()
        # logging.info(all_list)
        # logging.info([(t.tattooso, t.tattoo.owner, user) for t in all_list])
        return_list = list(filter(lambda x: x.user == user, all_list))
        # logging.info("Darova")
        # logging.info([(t.tattoo, t.tattoo.owner) for t in return_list])
        return return_list

# class TattooImageDetail(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, pk):
#         try:
#             return TattooImage.objects.get(pk=pk)
#         except TattooImage.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = TattooImageSerializer(snippet)
#         return Response(serializer.data)


# class TattooImageSave(APIView):
#     permission_classes = (IsAuthenticated,)

#     # def post(self, request, format=None):
#     #     data = request.data
#     #     data["owner"]


# class TattooImageDirect(APIView):
#     def get(self, request, img_path):
#         path = os.path.join(settings.MEDIA_ROOT, TattooImageDirect.img_path)

#         try:
#             with open(path, "rb") as img_file:
#                 return HttpResponse(img_file.read(), content_type="image/jpeg")
#         except IOError:
#             red = PIL.Image.new('RGBA', (1, 1), (255, 0, 0, 0))
#             response = HttpResponse(content_type="image/jpeg")
#             red.save(response, "JPEG")
#             return response


# class TattooImageViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.

#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = TattooImage.objects.all()
#     serializer_class = TattooImageSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     # def highlight(self, request, *args, **kwargs):
#     #     snippet = self.get_object()
#     #     return Response(snippet.highlighted)

#     def perform_create(self, serializer):
#         serializer.save(name=self.request.name, owner=self.request.user)


# OAuth2 ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# def index(request):
#     from blog.tasks import add
#     print(111)
#     add.delay(7,9)
#     print(111)
#     return render(request, 'index.html')


# def signup(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/')

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             User.objects.create_user(username=username, email=email, password=password)
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponseRedirect('/login')
#     else:
#         form = SignUpForm()

#     return render(request, 'signup.html', {'form': form})


# def login(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/')

#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponseRedirect('/login')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


# def logout(request):
#     auth_logout(request)
#     return HttpResponseRedirect('/login')
