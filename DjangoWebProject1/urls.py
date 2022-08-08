"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include, url
import testDjango1.views


urlpatterns = [
    url(r'^$', testDjango1.views.index, name='index'),
    url(r'^home$', testDjango1.views.index, name='home'),
]
