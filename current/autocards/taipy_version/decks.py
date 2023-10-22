from classes import *
from taipy.gui import navigate
import browse
decks_df = getDecksDB()

def decks_clicked(state, var_name, action, payload):
    browse.deck_name = decks_df[payload['index']]
    
    navigate(state, "browse")

decks_md = """
<|{decks_df}|table|on_action=decks_clicked|>
"""