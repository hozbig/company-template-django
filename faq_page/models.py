from django.db import models

# Create your models here.
class FaqSubject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


class FaqQuestion(models.Model):
    question = models.CharField(max_length=120)
    awnser =  models.TextField()
    subject = models.ManyToManyField(FaqSubject, related_name="faq_rel_name")

    def __str__(self):
        return self.question