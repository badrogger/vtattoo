"""vtattoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import os
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from tattoo import views
from django.conf.urls.static import static

from django.conf import settings

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^tattoo-index/$', views.TattooIndexList.as_view()),
    url(r'^tattoo-upload/$', views.TattooCreate.as_view()),
    url(r'^tattoo-studios/$', views.StudioList.as_view()),
    url(r'^tattoo-users/$', views.UserTattooList.as_view()),
    url(r'^deals/$', views.DealList.as_view()),
    # url(r'^image-upload/$', views.FileUploadView.as_view()),
    # url(r'^tattoo-images/(?P<pk>[0-9]+)/$', views.TattooImageDetail.as_view()),
    # url(r'^', include(router.urls)),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^api-auth/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=os.path.join(settings.MEDIA_ROOT, "tattooimg"))
