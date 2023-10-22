from django.urls import path
from . import views

urlpatterns = [
    path('browse_cards/<str:deck_name>/', views.get_cards, name='browse_cards'),
    path('browse_decks/', views.get_decks, name="browse_decks"),
    path('edit_deck/<str:deck_name>/', views.edit_deck, name='edit_deck'),
    path('add_deck/', views.add_deck, name='add_deck'),
    path('add_card/', views.add_card, name="add_card"),
    path('set_generator/', views.generate_user_input, name="set_generator"),
]