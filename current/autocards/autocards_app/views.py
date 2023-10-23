from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.http import Http404

def get_cards(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cards = Card.objects.filter(Q(question__icontains=q) | Q(answer__icontains=q))
    context = {'cards': cards}
    return render(request, 'browse_decks.html', context)

def add_card(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/autocards_app/list')

    context = {'form': form}
    return render(request, 'add_deck.html', context)

def edit_card(request, pk):
    card = Card.objects.get(id=pk)
    form = CardForm(instance=card)
 #I love you So. Much
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

def add_deck(request):
    form = DeckForm()
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('browse_decks')

    context = {'form': form}

def sort_by_spacing(request):
    Card._meta.ordering = ["spacing", "next_due"]
    return redirect('browse_decks')

def sort_by_next_due(request):
    Card._meta.ordering = ["next_due", "spacing"]
    return redirect('browse_decks')

def review(request, deck_id, card_id):
    #try:
    card = Deck.objects.get(name=deck_id).cards.get(id=card_id)
    context = {'card': card, 'card_id': card_id}
    #except Card.DoesNotExist:
        #raise Http404("Question does not exist")
    return render(request, 'review.html', context)

