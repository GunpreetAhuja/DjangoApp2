from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'randomz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^shop/', include('shop.urls')),
    #url(r'^shop/display/', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
