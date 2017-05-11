# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Ogloszenia

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Ogloszenia)), name='lista'),
    url(r'^dodaj/$', views.OgloszenieCreate.as_view(), name='dodaj'),
    url(r'^edytuj/(?P<pk>\d+)/', views.OgloszenieUpdate.as_view(), name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', views.OgloszenieDelete.as_view(), name='usun'),
    url(r'^info/(?P<pk>\d+)/', views.OgloszenieDetailView.as_view(), name='info'),
]