from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.layout.views import index

admin.site.site_header = 'Daily Manager'
admin.site.site_title = 'Daily Manager'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('orders/', include('core.managers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
