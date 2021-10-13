from django.db import models

# Create your models here.
class Article(models.Model):
    # MAIN FILED:
    title = models.CharField(max_length=150, )
    slug = models.SlugField(blank=True, default="", unique=True, )
    text = models.TextField(null=True, blank=True, )
    image = models.ImageField(upload_to="articles-image/", null=True, blank=False, )
    time_for_read = models.IntegerField(default=5)
    # category = models.ManyToManyField(Category, , related_name="papers")

    # RESOURCE:
    # author = models.CharField(max_length=30, default="no-author", null=True, blank=True, )
    # author_image = models.URLField(null=True, blank=True, default="", help_text="Let it blank to don not display.", )
    # author_describe = models.CharField(max_length=200, null=True, blank=True, )

    # TIMES:
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, )
    publish_time = models.DateTimeField(auto_now=True, blank=True, null=True, )

    # STATUS FIELD:
    STATUS_LIST = (
            ("p", "publish"),
            ("d", "draft"),
        )
    status = models.CharField(max_length=1, choices=STATUS_LIST, default="p", )
    suggest = models.BooleanField(default=False, help_text="If true: avaibale to show in suggest field.", )

    def __str__(self):
        return f"{self.id}.{self.title}"
