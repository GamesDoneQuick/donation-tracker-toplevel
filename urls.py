from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/lookups/', include('ajax_select.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'tracker.views.logout'),
)

try:
    import imp
    imp.find_module('tracker_ui')
    urlpatterns += patterns('', url(r'^ui/', include('tracker_ui.urls')))
except ImportError:
    print("Could not locate tracker_ui module, starting without it")
