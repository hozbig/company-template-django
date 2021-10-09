from django.shortcuts import render


# home view
def home_view(request):
    context = {
        "page_title": "خانه",
    }
    return render(request, 'home/home.html', context)
