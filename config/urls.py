from django.contrib import admin
from django.urls import path, include

# for statics,media files
from django.conf import settings
from django.conf.urls.static import static

app_name = 'url'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls'), name= 'home'),
]

if settings.DEBUG:
    # add root 'static' files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add root 'media' files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
