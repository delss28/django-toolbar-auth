from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from clinic import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('services/', include('services.urls', namespace='services')),
    path('user/', include('users.urls', namespace='user')),
] 

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)