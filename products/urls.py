from django.conf.urls import url,include
from django.contrib import admin
from products import views
from django.views.generic import RedirectView
urlpatterns = [
    # url(r'^antiguatuor/',views.landing,name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]