from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^authenticate/$', views.authenticate, name='authenticate'),
    url(r'^(?P<slug>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[0-9]+)/vote/$', views.vote, name='vote'),
]
