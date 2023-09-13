# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import  WordleSquare

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #Select Word
    x = random.randint(0,len(FIVE_LETTER_WORDS))
    word = FIVE_LETTER_WORDS[x].upper()

    def generateWord():
        x = random.randint(0,len(FIVE_LETTER_WORDS))
        gameWord = FIVE_LETTER_WORDS[x].upper()
        return gameWord
        
    #show word to check
    gw.set_wrod(word)
    
    #Check if word is valid
    if word not in FIVE_LETTER_WORDS:
        gw.show_message("Please Enter a Valid Word")
    
    #Convert word to letters and place in first row
    for x in range(0,N_COLS):
        gw.set_square_letter(0,x,word[x])
    

# Startup code

if __name__ == "__main__":
    wordle()
