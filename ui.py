from taipy import *
from taipy.gui import Markdown
from decks import *
from browse import *
from classes import *
pages = {
    '/': Markdown("<|navbar|>"),
    'browse': Markdown(browse_md),
    'decks': Markdown(decks_md)  
}
Gui(pages=pages).run()