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
        row = gw.get_current_row()
        guess = ""
        valid = False
        for l in range(0, N_COLS):
            guess = guess + gw.get_square_letter(row,l)
        valid = check_word(guess,valid)
        
        if valid == True:    
            row = row + 1
        row = gw.set_current_row(row)

  
        
        
    
    gw = WordleGWindow()
    row = 0
    gw.add_enter_listener(enter_action)
       
    gw.set_current_row(row)
    
    #Select Word


    def generateWord():
        x = random.randint(0,len(FIVE_LETTER_WORDS))
        gameWord = FIVE_LETTER_WORDS[x].upper()
        return gameWord
        
    word = generateWord()
    

    #Check if word is valid
    def check_word(guess,valid):
        guess = guess.lower()
        if guess not in FIVE_LETTER_WORDS:
            valid = False
            gw.show_message("Not in word list")
        else:
            gw.show_message("So far, so good")
            valid = True
        return valid
    
    #Convert word to letters and place in first row
    # for x in range(0,N_COLS):
    #     gw.set_square_letter(0,x,word[x])


    

# Startup code

if __name__ == "__main__":
    wordle()
