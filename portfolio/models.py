from django.db import models
from extensions.myUtilsForJalali import jalali_convertor

# Create your models here.
class Portfolio(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=50, default="")
	description1 = models.TextField()
	image1 = models.ImageField(upload_to='portfolio-image/', null=False, blank=False)
	image2 = models.ImageField(upload_to='portfolio-image/', null=True, blank=True)
	image3 = models.ImageField(upload_to='portfolio-image/', null=True, blank=True)
	description2 = models.TextField(null=True, blank=True)
	# TIMES:
	created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	publish_time = models.DateTimeField(auto_now=True, blank=True, null=True)
	# STATUS FIELD:
	STATUS_LIST = (
			("p", "publish"),
			("d", "draft"),
		)
	status = models.CharField(max_length=1, choices=STATUS_LIST, default="p", )
	suggest = models.BooleanField(default=False)

	# TIME CONVERTOR TO JALALI FORMAT:
	def j_created_time(self):
		return jalali_convertor(self.created_time, lang_format="en", time_status="on")
	j_created_time.short_description = "created_time"
	def j_publish_time(self):
		return jalali_convertor(self.publish_time)
	j_publish_time.short_description = "published_time"
