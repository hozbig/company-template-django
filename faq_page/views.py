from django.shortcuts import render


# faq view
def faq_view(request):
    context = {
        "page_title": "سوالات متداول",
    }
    return render(request, 'faq/faq.html', context)