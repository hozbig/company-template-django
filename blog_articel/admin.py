from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'status', 'suggest', 'j_created_time']
    list_filter = ["status", "suggest", "created_time"]
    search_fields = ['title',]
    ordering = ['-created_time']

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)