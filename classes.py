import json
import pandas as pd

def getDeckDB(deck_name):
    try:
        with open(f"data/{deck_name}.json") as file:
            db = json.load(file)
    except:
        db = []
    return db

def getDeckDF(deck_name):
    return pd.DataFrame.from_records(getDeckDB(deck_name))

df = getDeckDF("deck1")
print(df)

def editCard(deck_name, card_id, column_name, new_value):
    db = getDeckDB(deck_name)

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
    db = getDeckDB(deck_name)

    db.pop(card_id)

    try:
        with open(f"data/{deck_name}.json", "w") as file:
            json.dump(db, file, indent="    ")
    except:
        pass
    print("card deleted")

def addCard(deck_name):
    db = getDeckDB(deck_name)

    db.append({})
    db[-1]["question"] = ""
    db[-1]["answer"] = ""
    db[-1]["next_due"] = ""
    db[-1]["spacing"] = ""

    try:
        with open(f"data/{deck_name}.json", "w") as file:
            json.dump(db, file, indent="    ")
    except:
        pass
