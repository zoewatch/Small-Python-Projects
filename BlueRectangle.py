# File: BlueRectangle.py

"""
Created on Mon Mar 23 14:50:58 2020

@author: zoewatch
"""

from pgl import GWindow, GOval, GRect, GLine

# Constants

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 900


# Main program


gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
oval = GOval(150, 150, 120, 20)
oval.setFilled(False)
oval.setColor("Pink")
gw.add(oval) 
oval2 = GOval(170, 75, 30, 50)
oval2.setFilled(True)
oval2.setColor("Green")
gw.add(oval2)
oval3 = GOval(220, 75, 30, 45)
oval3.setFilled(True)
oval3.setColor("Red")
gw.add(oval3)
rect = GRect(140, 60, 140, 160)
rect.setFilled(False)
rect.setColor("Gray")
gw.add(rect)
neck = GLine(200, 700, 200, 200)
gw.add(neck)
arms = GLine(200, 200, 100, 200)
gw.add(arms)
cubism = GLine(200, 500, 400, 100)
gw.add(cubism)
    
    
    
