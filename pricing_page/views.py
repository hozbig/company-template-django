from django.shortcuts import render


# pricing view
def pricing_view(request):
    context = {
        "page_title": "پلن ها",
    }
    return render(request, 'pricing/pricing.html', context)
