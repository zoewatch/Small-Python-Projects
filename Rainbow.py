#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:48:20 2020

@author: zoewatch
"""

from pgl import GWindow, GRect, GOval


# Constants

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
ONE_RAINBOW_RADIUS = 450
TWO_RAINBOW_RADIUS = 430
THREE_RAINBOW_RADIUS = 410
FOUR_RAINBOW_RADIUS = 390
FIVE_RAINBOW_RADIUS = 370
SIX_RAINBOW_RADIUS = 350
SEVEN_RAINBOW_RADIUS = 330
EIGHT_RAINBOW_RADIUS = 310



def createRainbow():
    gw = GWindow (GWINDOW_WIDTH, GWINDOW_HEIGHT)
    rect = GRect (0,0, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    rect.setFilled(True)
    rect.setFillColor("cyan")
    rect.setColor("cyan")
    gw.add(rect)
    cx = gw.getWidth() / 2
    cy = gw.getHeight()
    gw.add(createFilledCircle(cx, cy, ONE_RAINBOW_RADIUS/1.05, "red"))
    gw.add(createFilledCircle(cx, cy, TWO_RAINBOW_RADIUS/1.05, "orange"))
    gw.add(createFilledCircle(cx, cy, THREE_RAINBOW_RADIUS/1.05, "yellow"))
    gw.add(createFilledCircle(cx, cy, FOUR_RAINBOW_RADIUS/1.05, "green"))
    gw.add(createFilledCircle(cx, cy, FIVE_RAINBOW_RADIUS/1.05, "blue"))
    gw.add(createFilledCircle(cx, cy, SIX_RAINBOW_RADIUS/1.05, "indigo"))
    gw.add(createFilledCircle(cx, cy, SEVEN_RAINBOW_RADIUS/1.05, "violet"))
    gw.add(createFilledCircle(cx, cy, EIGHT_RAINBOW_RADIUS/1.05, "cyan"))

def createFilledCircle(x, y,r,color):
    circle = GOval (x - r, y - r/1.5, 2 * r, 2 * r)
    circle.setColor (color)
    circle.setFilled(True)
    return circle




def rainbow():
    GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    
    createRainbow()

if __name__ =="__main__":
    rainbow()
    