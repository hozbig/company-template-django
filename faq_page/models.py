from django.db import models

# Create your models here.
class FaqQuestion(models.Model):
    question = models.CharField(max_length=120)
    awnser =  models.TextField()

    def __str__(self):
        return self.question


class FaqSubject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.IntegerField()
    fa_question = models.ManyToManyField(FaqQuestion, related_name="que_rel_name")

    def __str__(self):
        return f"{self.id}. {self.title}"