from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'category_to_str', 'status', 'suggest', 'j_created_time']
    list_filter = ["status", "suggest", "created_time"]
    search_fields = ['title',]
    ordering = ['-created_time']

    def category_to_str(self, obj):
        return " - ".join([category.title for category in obj.category.all()])
        # return " - "

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)