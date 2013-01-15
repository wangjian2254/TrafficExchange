from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.contrib import admin
from TrafficExchange import settings
from TrafficExchange.traffic.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'TrafficExchange.views.home', name='home'),
    url(r'^$', index),
    # url(r'^TrafficExchange/', include('TrafficExchange.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
