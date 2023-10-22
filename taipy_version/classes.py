import json
import os
import pandas as pd
from pathlib import Path

def getCardsDB(deck_name):
    try:
        with open(f"data/{deck_name}.json") as file:
            db = json.load(file)
    except:
        db = []
    return db

def getCardsDF(deck_name):
    return pd.DataFrame.from_records(getCardsDB(deck_name))

def editCard(deck_name, card_id, column_name, new_value):
    db = getCardsDB(deck_name)

    print(db)
    print(f"changing {card_id}, {column_name} to {new_value}")
    db[card_id][column_name] = new_value

    try:
        with open(f"data/{deck_name}.json", "w") as file:
            json.dump(db, file, indent="    ")
    except:
        pass
    print("card updated")
    
def deleteCard(deck_name, card_id):
    db = getCardsDB(deck_name)

    db.pop(card_id)

    try:
        with open(f"data/{deck_name}.json", "w") as file:
            json.dump(db, file, indent="    ")
    except:
        pass
    print("card deleted")

def addCard(deck_name):
    db = getCardsDB(deck_name)

    db.append({})
    db[-1]["question"] = ""
    db[-1]["answer"] = ""
    db[-1]["next_due"] = -1
    db[-1]["spacing"] = -1

    try:
        with open(f"data/{deck_name}.json", "w") as file:
            json.dump(db, file, indent="    ")
    except:
        pass


def getDecksDB():
    data_dir = Path("data")
    file_names = [x.stem for x in data_dir.iterdir()]
    return file_names