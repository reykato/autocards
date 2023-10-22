from django.db import models
import time

# Create your models here.

# Create your models here.
class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    next_due = models.IntegerField()
    spacing = models.IntegerField()

    class Meta:
        ordering = ["next_due", "id"]

    def __str__(self):
        return f"{self.id} {self.question} : {self.answer}"
    
class Deck(models.Model):
    name = models.TextField()
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return f"{self.name}"
    

def add_new_card_to_db(question, answer):
    card = Card()
    card.question = question
    card.answer = answer
    card.next_due = time.time()
    card.spacing = 0
    card.save()
    return card.pk