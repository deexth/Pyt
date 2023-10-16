from django.db import models

# Create your models here.
class Prompt(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question