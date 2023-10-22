from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Card
from .forms import CardForm
from django.db.models import Q
from . import set_generator

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

def generate_user_input(request):
    if(request.method == 'POST'):
        try:
            prompt = request.POST.get('input1')
            deck_size = int(request.POST.get('input2'))
            set_generator.retrieve_deck_json(prompt, deck_size)
        except Exception as e:
            print(str(e))
    context = {}
    return render(request, 'set_generator.html', context)