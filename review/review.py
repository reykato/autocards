#Make UI for reviewing flash cards
from taipy import Gui

# A dark mode is available in Taipy
# However, we will use the light mode for the Getting Started
Gui(page="# Getting started with *Taipy*").run(dark_mode=True)