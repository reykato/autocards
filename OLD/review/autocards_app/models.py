from django.db import models

# Create your models here.
class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    next_due = models.IntegerField()
    spacing = models.IntegerField()

    class Meta:
        ordering = ["name", "id"]