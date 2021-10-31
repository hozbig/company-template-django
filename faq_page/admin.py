from django.contrib import admin
from .models import FaqSubject, FaqQuestion

# Register your models here.
class FaqSubjectAdmin(admin.ModelAdmin):
    ordering = ["position"]

    class Meta():
        model = FaqSubject
admin.site.register(FaqSubject, FaqSubjectAdmin)


class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "question"]
    ordering = ["subject"]

    class Meta():
        model = FaqSubject
admin.site.register(FaqQuestion, FaqQuestionAdmin)