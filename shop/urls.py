from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('',
    url(r'^$', views.display),
    url(r'^display/', views.display, name='display'),
)
