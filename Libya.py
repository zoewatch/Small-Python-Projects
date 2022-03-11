
from pgl import GWindow, GRect

def libya():
    gw = GWindow(600, 400)
    rect = GRect (150, 100, 300, 200)
    rect.setFilled(True)
    rect.setFillColor("green")
    rect.setColor("green")
    gw.add(rect)
    


if __name__ =="__main__":
    libya()
        # -*- coding: utf-8 -*-

