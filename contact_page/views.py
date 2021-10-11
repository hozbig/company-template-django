from django.shortcuts import render


# contact view
def contact_view(request):
    context = {
        "page_title": "تماس با ما",
    }
    return render(request, 'contact/contact.html', context)
