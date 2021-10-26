from django.shortcuts import render
from blog_articel.models import Article


# blog_home view
def blog_home_view(request):
    articeles = Article.objects.all().order_by("-created_time").filter(suggest=True)[:3]
    last_articel = Article.objects.all()
    context = {
        "page_title": "وبلاگ",
        'articeles': articeles,
        'last_articel': last_articel[len(last_articel)-1:],
    }
    return render(request, 'blog/blog-home.html', context)


# blog_post view
def blog_post_view(request, slug):
    try:
        articel = Article.objects.all().get(slug=slug)
        templateName = 'blog/blog-post.html'
    except:
        articel = None
        templateName = "blog/blog-post.html"
    context = {
        "page_title": articel.title,
        "articel": articel,
    }
    return render(request, templateName, context)

# blog_list view
def blog_list_view(request):
    articeles = Article.objects.all().order_by("-created_time")
    context = {
        "page_title": "لیست مقالات",
        'articeles': articeles,
    }
    return render(request, 'blog/blog-list.html', context)

# blog_list_suggests view
def blog_list_suggests_view(request):
    articeles = Article.objects.all().order_by("-created_time")
    context = {
        "page_title": "لیست مقالات ویژه",
        'articeles': articeles,
    }
    return render(request, 'blog/blog-list-suggests.html', context)
