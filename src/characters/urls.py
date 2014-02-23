from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterView.as_view(), name='character-detail'),
    url(r'^create/', views.CharacterCreateView.as_view(), name='create-character')
)
