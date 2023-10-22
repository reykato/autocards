from django.forms import ModelForm
from .models import *

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'