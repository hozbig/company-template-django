from django import template
from blog_articel.models import Article

register = template.Library()

@register.inclusion_tag("partials/last-articeles.html")
def last_articeles_tag():
    return {
        'articeles': Article.objects.all().order_by("-created_time"),
    }
