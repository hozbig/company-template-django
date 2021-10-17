from django.shortcuts import render
from blog_articel.models import Article

# home view
def home_view(request):
    articeles = Article.objects.all().filter(suggest=True)[:3]
    context = {
        "page_title": "خانه",
        'articeles': articeles,
    }
    return render(request, 'home/home.html', context)
