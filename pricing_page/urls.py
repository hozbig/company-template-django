from django.urls import path
from .views import pricing_view

app_name = 'pricing_app'
urlpatterns = [
    path('', pricing_view, name= 'pricing_url'),
]