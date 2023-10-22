from django.urls import path
from . import views

urlpatterns = [
    path('browse_decks/', views.get_cards, name="list"),
    path('card_form/', views.add_card, name="itemform"),
    path('sortbynextdue/', views.sort_by_next_due, name="sortbyid"),
    path('sortbyspacing/', views.sort_by_spacing, name="sortbyname"),
    path('set_generator/', views.generate_user_input, name="set_generator")
]