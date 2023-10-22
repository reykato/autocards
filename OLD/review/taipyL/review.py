#Make UI for reviewing flash cards
from taipy import Gui
import time
import requests
import json
import os


# A dark mode is available in Taipy
# However, we will use the light mode for the Getting Started

def on_change(state, var_name: str, var_value):
    if var_name == "card": 
        card = int(var_value)

def updateShow(state):
    state.cardQ = deck[state.card]["question"]
    state.card = state.card + 1
    
    if state.card >= len(deck):
        state.card = 0
    

def grabCards(url):
    #location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(url)))
    file = open(url)
    deck = json.load(file)
    file.close()
    return deck

def close(state):
    print("close")

page = """
**<h1 style="text-align: center;">Reviewing</h1>**

<|Sets|button|onAction=close|>

-------
<center><|{card}|></center>
<center><|{cardQ}|></center>
----
<|Flip|button|on_action=updateShow|>






"""
card = 0
cardQ = ""
deck = grabCards('./review/deck1.json')
cardQ = deck[0]["question"]
Gui(page).run(dark_mode=True, use_reloader=True, port=5001)
