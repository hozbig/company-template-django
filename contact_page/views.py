from django.shortcuts import render
from .form import ContactUsPageForm
from .models import ContactUsPageModel

# contact view
def contact_view(request):
    form = ContactUsPageForm()
    if request.method == "POST":
        form = ContactUsPageForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            p = ContactUsPageModel(full_name=full_name, email=email, phone_number=phone_number, message=message)
            p.save()
            form = ContactUsPageForm()
            context = {
                "form": form,
                "page_title": "تماس با ما",
            }
    context = {
        "form": form,
        "page_title": "تماس با ما",
    }
    return render(request, 'contact/contact.html', context)
