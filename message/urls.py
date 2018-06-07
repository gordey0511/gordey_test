from django.conf.urls import url, include
from django.contrib import admin
from message import views

urlpatterns = [

    url(r'^message/$', views.message, name='message'),
]