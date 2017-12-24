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

from tattoo import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^tattoo-index/$', views.TattooIndexList.as_view()),
    url(r'^tattoo-upload/$', views.TattooCreate.as_view()),
    url(r'^tattoo-studios/$', views.StudioList.as_view()),
    url(r'^tattoo-users/$', views.UserTattooList.as_view()),
    url(r'^deals/$', views.DealList.as_view()),
    url(r'^tattoo-studios/(?P<pk>[0-9]+)/$', views.StudioDetail.as_view()),
    url(r'^code-deal/$', views.DealDetail.as_view()),
    url(r'^update-deal/(?P<pk>[0-9]+)/$', views.DealUpdate.as_view()),
] + static(settings.MEDIA_URL, document_root=os.path.join(settings.MEDIA_ROOT, "tattooimg"))
