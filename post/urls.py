from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^load/$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_single, name="post_single")
]
