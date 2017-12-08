# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from blog.forms import LoginForm, SignUpForm
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, Group
from tattoo.models import TattooImage
from rest_framework import viewsets, permissions
from tattoo.serializers import UserSerializer, GroupSerializer
from tattoo.serializers import TattooImageSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
# from oauth2_provider.contrib.rest_framework import TokenHasScope


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


class TattooImageList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        tattoo_images = TattooImage.objects.all()
        serializer = TattooImageSerializer(tattoo_images, many=True)
        return Response(serializer.data)


class TattooImageDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return TattooImage.objects.get(pk=pk)
        except TattooImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TattooImageSerializer(snippet)
        return Response(serializer.data)


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
