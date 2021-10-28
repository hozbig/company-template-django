from django.contrib import admin
from .models import ContactUsPageModel

# Register your models here.
class ContactUsPageModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone_number', 'message', 'created_time']
    list_filter = ["email", "phone_number", "created_time"]
    search_fields = ["email", "phone_number",]
    ordering = ['-created_time']

    class Meta:
        model = ContactUsPageModel

admin.site.register(ContactUsPageModel, ContactUsPageModelAdmin)