from django.urls import path
from . import views

urlpatterns = [
    path('browse_decks/', views.get_cards, name="list"),
    path('card_form/', views.add_card, name="itemform"),
    path('sortbynextdue/', views.sort_by_next_due, name="sortbyid"),
    path('sortbyspacing/', views.sort_by_spacing, name="sortbyname"),
    path('add_deck/', views.add_deck, name='add_deck'),
    path("review/<str:deck_id>/<int:card_id>/", views.review, name="review"),
]