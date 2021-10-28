from django.db import models
from django.forms import ModelForm

# Create your models here.
class ContactUsPageModel(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=75)
    message = models.TextField()
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "messages"

    def __str__(self) -> str:
        return f"{self.full_name}"


class SubscribeForm(ModelForm):
    class Meta:
        model = ContactUsPageModel
        exclude = ('created_time',)