from django.shortcuts import render
from .models import FaqSubject
# faq view
def faq_view(request):
    subjects = FaqSubject.objects.all()
    context = {
        "page_title": "سوالات متداول",
        'subjects': subjects,
    }
    return render(request, 'faq/faq.html', context)