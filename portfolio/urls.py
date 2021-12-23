from django.urls import path
from .views import portfolio_home_view, portfolio_post_view

app_name = 'portfolio_app'
urlpatterns = [
    path('', portfolio_home_view, name= 'portfolio_home_url'),
    path('<slug>', portfolio_post_view, name= 'portfolio_post_url'),
]