# convert pounds into kilograms
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
import pylint

def lbs_to_kg(lbs):
    return lbs/2.204624420

lbs = 164.5
lbs_to_kg(lbs)
# interact (lbs_to_kg, lbs=lbs)
