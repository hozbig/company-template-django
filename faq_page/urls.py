from django.urls import path
from .views import faq_view

app_name = 'faq_app'
urlpatterns = [
    path('', faq_view, name= 'faq_url'),
]