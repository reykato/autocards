from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from .set_generator import generate_json_file, retrieve_deck_json
import time

def get_cards(request, deck_name):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cards = Deck.objects.get(name=deck_name).cards.all()
    context = {'cards': cards}
    return render(request, 'browse_cards.html', context)

def get_decks(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    decks = Deck.objects.filter(Q(name__icontains=q))
    context = {'decks' : decks}
    return render(request, "browse_decks.html", context)

def edit_deck(request, deck_name):
    deck = Deck.objects.get(name=deck_name)
    form = DeckForm(instance=deck)
    if request.method == 'POST':
        form = DeckForm(request.POST, instance = deck)
        if form.is_valid():
            form.save()
            return redirect('browse_decks')
    context = {'form' : form}
    return render(request, 'edit_deck.html', context)

def add_deck(request):
    form = DeckForm()
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('browse_decks')

    context = {'form': form}
    return render(request, 'add_deck.html', context)

def add_card(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('browse_cards')

    context = {'form': form}
    return render(request, 'add_deck.html', context)

def edit_card(request, pk):
    card = Card.objects.get(id=pk)
    form = CardForm(instance=card)
    if request.method == 'POST':
        form = CardForm(request.POST, instance = card)
        if form.is_valid():
            form.save()
            return redirect('browse_decks.html')

    context = {'form' : form}
    return render(request, 'card_form.html', context)

def delete_card(request, pk):
    card = Card.objects.get(id=pk)
    if request.method == 'GET':
        card.delete()
        return redirect('browse_decks')
    context = {}
    return render(request, 'browse_decks.html', context)

def update_card_interval(request, pk, new_next_due, new_spacing):
    card = Card.objects.get(id=pk)
    card.next_due = new_next_due
    card.spacing = new_spacing
    return card

def generate_user_input(request):
    if(request.method == 'POST'):
        try:
            prompt = request.POST.get('input1')
            deck_size = int(request.POST.get('input2'))
            deck_name = request.POST.get('input3')
            retrieve_deck_json(prompt, deck_size, deck_name)
            return redirect("browse_decks")
        except Exception as e:
            print(str(e))
    context = {}
    return render(request, 'set_generator.html', context)