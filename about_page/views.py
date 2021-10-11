from django.shortcuts import render


# about view
def about_view(request):
    context = {
        "page_title": "درباره ما",
    }
    return render(request, 'about/about.html', context)