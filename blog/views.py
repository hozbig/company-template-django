from django.shortcuts import render


# blog_home view
def blog_home_view(request):
    context = {
        "page_title": "وبلاگ",
    }
    return render(request, 'blog/blog-home.html', context)


# blog_post view
def blog_post_view(request):
    context = {
        "page_title": "پست",
    }
    return render(request, 'blog/blog-post.html', context)