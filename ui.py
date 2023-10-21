from taipy import *
from taipy.gui import Markdown
from make_card import *
from browse import *
from classes import *
pages = {
    'review': Markdown(browse_md),
    'make_card': Markdown(make_card_md)  
}
Gui(pages=pages).run()