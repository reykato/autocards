from django.urls import path
from . import views

urlpatterns = [
    path('browse_cards/', views.get_cards, name="browse_cards"),
    path('browse_decks/', views.get_decks, name="browse_decks"),
    path('add_card/', views.add_card, name="add_card"),
    path('sortbynextdue/', views.sort_by_next_due, name="sortbyid"),
    path('sortbyspacing/', views.sort_by_spacing, name="sortbyname")
]