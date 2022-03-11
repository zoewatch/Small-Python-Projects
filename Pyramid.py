#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:34:39 2020

@author: zoewatch
"""

from pgl import GWindow, GRect

GWINDOW_WIDTH = 600
GWINDOW_HEIGHT = 400
BRICK_HEIGHT = 20
BRICK_WIDTH = 40
BRICKS_IN_BASE = 12
SPACE_BEFORE_BRICKS = 100

def createBackground():
    gw = GWindow (GWINDOW_WIDTH, GWINDOW_HEIGHT)
    cx = gw.getWidth() / 2
    cy = gw.getHeight()
    SPACE_BEFORE_BRICKS = 100
    rect = gw.add(GRect(cx, cy, BRICK_WIDTH, BRICK_HEIGHT)
    for i in range (1, 12, 2):
        print(" " * SPACE_BEFORE_BRICKS +i*(rect))
        SPACE_BEFORE_BRICKS = (SPACE_BEFORE_BRICKS - (0.5*BRICK_WIDTH))

    
def japan():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gw.add(createBackground())


    
    
if __name__ == "__main__":
    japan()