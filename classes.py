import json
import pandas as pd

with open("data/test.json") as file:
    db = json.load(file)

df = pd.DataFrame.from_records(db['deck1']).transpose()

print(df)