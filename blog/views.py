from django.shortcuts import render
from blog_articel.models import Article


# blog_home view
def blog_home_view(request):
    articeles = Article.objects.all().filter(suggest=True)
    context = {
        "page_title": "وبلاگ",
        'articeles': articeles,
    }
    return render(request, 'blog/blog-home.html', context)


# blog_post view
def blog_post_view(request):
    context = {
        "page_title": "پست",
    }
    return render(request, 'blog/blog-post.html', context)