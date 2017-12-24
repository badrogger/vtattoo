import random
import logging

from rest_framework import status
from django.contrib.auth.models import User, Group
from tattoo.models import Tattoo, Studio, Deal
from rest_framework import viewsets, permissions
from rest_framework import generics
from tattoo.serializers import UserSerializer, GroupSerializer
from tattoo.serializers import StudioSerializer, TattooSerializer, DealSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

logger = logging.getLogger(__name__)

logging.basicConfig(filename='views.log', level=logging.DEBUG)


def random_deal_code():
    return ''.join(str(random.randint(0, 9)) for i in range(20))


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TattooIndexList(generics.ListAPIView):
    queryset = Tattoo.objects.all()[:6]
    # queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer


class UserTattooList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        all_list = Tattoo.objects.all()
        logging.info(all_list)
        logging.info([(t.name, t.owner) for t in all_list])
        return_list = list(filter(lambda x: x.owner == user, all_list))
        return return_list

    serializer_class = TattooSerializer


class TattooCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

    def perform_create(self, serializer):
        t_file = self.request.data.get('file')
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


class StudioDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


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
        all_list = Deal.objects.all()
        return_list = list(filter(lambda x: x.user == user, all_list))
        return return_list


class DealDetail(APIView):

    def post(self, request, format=None):
        rcode = request.data["code"]
        deals = Deal.objects.all()
        rdeals = list(filter(lambda d: d.deal_code == rcode, deals))
        if len(rdeals) > 0:
            serializer = DealSerializer(rdeals[0])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealUpdate(generics.UpdateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
