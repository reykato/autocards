import json
import pandas as pd

with open("data/test.json") as file:
    db = json.load(file)

df = pd.DataFrame.from_records(db['deck1']).transpose()

def updateCard(card_id, column_name, new_value):
    with open("data/test.json", "r") as file:
        db = json.load(file)

    db[card_id][column_name] = new_value
    
    with open("data/test.json", "w") as file:
        json.dump(db, file)
    

