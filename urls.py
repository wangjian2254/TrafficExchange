from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.views import login, logout
from TrafficExchange import settings
from TrafficExchange.traffic.views import index
from TrafficExchange.traffic.loginviews import reg, reg2
from TrafficExchange.traffic.views import addWebSite, getCode, dataAnalytics, trafficSettings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'TrafficExchange.views.home', name='home'),
    url(r'^$', index),
    # url(r'^TrafficExchange/', include('TrafficExchange.foo.urls')),
    # traffic
    (r'^addWebSite/$',addWebSite),
    (r'^saveWebSite/$',saveWebSite),
    (r'^getCode/$',getCode),
    (r'^dataAnalytics/$',dataAnalytics),
    (r'^trafficSettings/$',trafficSettings),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # User reg or login
    (r'^Reg/$',reg),
    (r'^Reg2/$',reg2),
    (r'^accounts/login/$',login,{'template_name':'login1.html','redirect_field_name':'/'}),
    (r'^accounts/logout/$', logout,{'template_name':'logout.html'}),
    (r'^accounts/profile/$',index),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
