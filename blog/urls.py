from django.urls import path
from .views import blog_home_view, blog_post_view, blog_list_view

app_name = 'blog_app'
urlpatterns = [
    path('', blog_home_view, name= 'blog_home_url'),
    path('list', blog_list_view, name= 'blog_list_url'),
    path('<slug>', blog_post_view, name= 'blog_post_url'),
]