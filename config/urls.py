from django.contrib import admin
from django.urls import path, include

# for statics,media files
from django.conf import settings
from django.conf.urls.static import static

app_name = 'url'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls'), name= 'home'),
    path('about', include('about_page.urls'), name= 'about'),
    path('contact', include('contact_page.urls'), name= 'contact'),
    path('pricing', include('pricing_page.urls'), name= 'pricing'),
    path('faq', include('faq_page.urls'), name= 'faq'),
    path('blog', include('blog.urls'), name= 'blog'),
]

if settings.DEBUG:
    # add root 'static' files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add root 'media' files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
