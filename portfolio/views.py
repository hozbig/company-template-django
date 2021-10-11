from django.shortcuts import render


# blog_home view
def portfolio_home_view(request):
    context = {
        "page_title": "نمونه کارها",
    }
    return render(request, 'portfolio/portfolio-home.html', context)


# portfolio_post view
def portfolio_post_view(request):
    context = {
        "page_title": "نمونه",
    }
    return render(request, 'portfolio/portfolio-post.html', context)