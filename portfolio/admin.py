from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['title', 'status', 'suggest', 'j_created_time']
	list_filter = ["status", "suggest", "created_time"]
	search_fields = ['title',]
	ordering = ['-created_time']

	class Meta:
		model = Portfolio

admin.site.register(Portfolio, PortfolioAdmin)