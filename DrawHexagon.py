

# File: SpellingBee.py

"""
This program provides the basic framework for the SpellingBee program
you need to implement for Project #2.  Be sure to change this comment
so that it describes your program rather than the starter file.
"""

from english import ENGLISH_WORDS
from pgl import GWindow, GCompound, GPolygon, GLabel

# Constants

GWINDOW_WIDTH = 1000            # These constants specify the width
GWINDOW_HEIGHT = 300            # and height of the graphics window

BEEHIVE_X = 150                 # These constants specify the center
BEEHIVE_Y = 150                 # of the beehive figure

HEX_SIDE = 40                   # The length of a hexagon side
HEX_SEP = 76                    # The distance between hexagon centers
HEX_LABEL_DY = 14               # Offset to the label baseline

WORDLIST_X = 300                # Starting x coordinate of the wordlist
WORDLIST_Y = 20                 # Baseline of first word listed
WORDLIST_DX = 120               # Separation between wordlist columns
WORDLIST_DY = 17                # Separation between wordlist rows
SCORE_BASELINE = 10             # Distance from bottom to score baseline
SCORE_WORDLIST_SEP = 20         # Spacing between wordlist and scores

LABEL_FONT = "36px bold 'Helvetica Neue','Sans-Serif'"
WORDLIST_FONT = "16px 'Helvetica Neue','Sans-Serif'"
CENTER_HEX_COLOR = "#FFCC33"
OUTER_HEX_COLOR = "#DDDDDD"
PANGRAM_COLOR = "Blue"

# Main program

def wordAppearsInPuzzle (word, puzzle):
    if len(word) >= 4:
        for letter in word:
            if letter not in puzzle:
                return False
        if puzzle[0] in word:
            return True
    
def SpellingBee():
    puzzle = "AZDIRWY"
    print("Words appearing in " + puzzle + ":")
    listSpellingBeeWordsOnConsole(puzzle)

def listSpellingBeeWordsOnConsole(puzzle):
    puzzle = puzzle.lower()
    for word in ENGLISH_WORDS:
        if wordAppearsInPuzzle(word, puzzle):
            print(word)
            
def userInputsLetter():
    


# Startup code

if __name__ == "__main__":
    SpellingBee()
