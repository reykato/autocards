from classes import *
from taipy.gui import navigate
decks_df = getDecksDF()

#<a href="/browse?name={nameofdeck}">
def decks_clicked(state, var_name, action, payload):
    #state.
    navigate(state, "browse")

decks_md = """
<|{decks_df}|table|on_action=decks_clicked|>
"""