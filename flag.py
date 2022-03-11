#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:17:14 2020

@author: zoewatch
"""

from pgl import GWindow, GRect, GOval


# Constants

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
RECT_HEIGHT = 150
RECT_WIDTH = 100

def createBackground(color):
    rect = GRect(0,0, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    rect.setFilled(True)
    rect.setFillColor(color)
    rect.setColor(color)
    return rect

def createSun(color):
    sun_width = GWINDOW_WIDTH/4
    rect = GOval(GWINDOW_HEIGHT/2 - sun_width/2,
                 GWINDOW_HEIGHT/2 - sun_width/2,
                 sun_width,
                 sun_width)
    rect.setFilled(True)
    rect.setFillColor(color)
    rect.setColor(color)
    return rect
    
def japan():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gw.add(createBackground("skyblue"))
    gw.add(createSun("yellow"))

    
    
if __name__ == "__main__":
    ()