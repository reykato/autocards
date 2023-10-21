from classes import *
import pandas as pd

def browse_on_edit(state, var_name, action, payload):
    cp = getattr(state, var_name).copy()
    cp.loc[payload["index"], payload["col"]] = payload["value"]
    updateCard(payload["index"], payload["col"], payload["value"])
    state.assign(var_name, cp)
    #notify(state, "I", f"Edited value from '{old_value}' to '{value}'. (index '{index}', column '{col}')")
 

browse_md = """
<|{df}|table|on_edit=browse_on_edit|>

"""