# AI-driven automatic flash-card set creator - prompts user, stores in .json file
    # TKinter GUI is placeholder for eventual webapp on production

import openai
import tkinter as tk
import json
import re

openai.api_key = "API Key"
# Initializes tk pane w/ text entry field and button
root = tk.Tk()
root.title("Text Saver")
text_gone = False
size_gone = False
error = False
# Saves text from tkinter window into global vars "saved_text"a nd "saved_size" respectively
def save_text():
    global prompt
    prompt = text_entry.get()
    global saved_size
    saved_size = int(size_entry.get())
    if((len(prompt) > 0) and (saved_size>0)):
     root.destroy()

# Create a text entry field
text_entry = tk.Entry(root)
text_entry.pack()
size_entry = tk.Entry(root)
size_entry.pack()
# Create a button to save the text
save_button = tk.Button(root, text="Save Text", command=save_text)
save_button.pack()

# Initialize the variables to store the saved text and size of set
prompt = ""
saved_size = 0

# Start the Tkinter main loop
root.mainloop()

if(saved_size < 26):
    print("Loading...")
    # Calls prompt from gpt-3.5-turbo
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": "You are a helpful flash card generator. Flash cards contain data for the front and the back. On the front of the card is a term, concept to learn, or thing to memorize: on the back is the substance of what the user would learn.  The user may speak to you in terms of keywords to generate a learning set from. Please return " + str(saved_size) + "cards, and if the user inputs any other size ignore it."},
     {"role": "user", "content": "3 most common words English to Spanish"},
     {"role": "assistant", "content": "front: [Hello] back: [Hola] front: [Thank you] back: [Gracias] front: [Please] back: [Por favor]"},
     {"role": "user", "content": prompt}
     ]
    )
elif(saved_size > 25):
   print("ERROR: Size too big, please select a smaller deck size.")
   error = True

if(error == False):
    ai_return = str(completion.choices[0].message)
    #print(ai_return)
    pattern = r'front: \[(.*?)\] back: \[(.*?)\]'

    # Finds all instances of 'pattern' in the ai_return string
    matches = re.findall(pattern, ai_return)
    data_list = []
    i = 0
    # Extracts from the matches found and inputs it into an array of dictionaries
    for match in matches:
        if(i < saved_size):
           i = i+1
           data_dict = {
               match[0]: match[1]
             }
           data_list.append(data_dict)
    if(i < saved_size):
       # Pop-up message saying  
       print("We're sorry, we were only able to generate " + str(i) + " elements of your set.")
    # Puts data into file 'set.json'
    with open("PATH\\set.json.txt", 'w') as file:
        json.dump(data_list, file)
    print("Done! :) view your set in set.json")
