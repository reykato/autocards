from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CardForm
from django.db.models import Q

def get_cards(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cards = Card.objects.filter(Q(question__icontains=q) | Q(answer__icontains=q))
    context = {'cards': cards}
    return render(request, 'browse_cards.html', context)

def get_decks(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    decks = Deck.objects.filter(Q(name__icontains=q))
    context = {'decks' : decks}
    return render(request, "browse_decks.html", context)

def add_card(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/autocards_app/browse_cards')

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

def sort_by_spacing(request):
    Card._meta.ordering = ["spacing", "next_due"]
    return redirect('browse_decks')

def sort_by_next_due(request):
    Card._meta.ordering = ["next_due", "spacing"]
    return redirect('browse_decks')