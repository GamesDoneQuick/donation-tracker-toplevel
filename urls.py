from django.conf.urls import include, url

from django.contrib import admin

import tracker.urls
import ajax_select.urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^tracker/', include(tracker.urls)),
    url(r'^admin/lookups/', include(ajax_select.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.MEDIA_URL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
