from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterView.as_view(), name='display_character')
)
