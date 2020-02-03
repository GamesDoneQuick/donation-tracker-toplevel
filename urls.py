import ajax_select.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import path, include

import tracker.urls

urlpatterns = [
    path('tracker/', include(tracker.urls)),
    path('admin/lookups/', include(ajax_select.urls)),
    path('admin/', admin.site.urls),
]

if settings.MEDIA_URL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('static/<path>', views.serve),
    ]
