from classes import *
import pandas as pd
from taipy.gui import notify

def browse_on_edit(state, var_name, action, payload):
    print(f"updating card: {payload}")
    editCard(state.deck_name, payload["index"], payload["col"], payload["value"])
    new_df = state.df.copy()
    new_df.loc[payload["index"], payload["col"]] = payload["value"]
    state.df = new_df
    notify(state, "I", "Edited card successfully.")

def browse_on_delete(state, var_name, action, payload):
    deleteCard(state.deck_name, payload["index"])
    state.df = state.df.drop(index=payload["index"])
    notify(state, "I", "Deleted card successfully.")

def browse_on_add(state, var_name, action, payload):
    addCard(state.deck_name)
    empty_row = pd.DataFrame([[None for _ in state.df.columns]], columns=state.df.columns)
    state.df = pd.concat([state.df, empty_row], axis=0, ignore_index=True)

    notify(state, "S", f"Added a new row.")

cards_df = getCardsDF("deck1")
browse_md = """
<|{cards_df}|table|on_edit=browse_on_edit|on_delete=browse_on_delete|on_add=browse_on_add|>
"""