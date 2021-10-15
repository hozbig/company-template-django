from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'position']
    search_fields = ['slug', 'title', 'position']
    ordering = ['position']

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)