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
    
    #Select Word
    def generateWord():
        gameWord = random.choice(FIVE_LETTER_WORDS)
        return gameWord
    
    gameWord = generateWord()
    print(gameWord)      


        #Check if word is valid
    def check_word(guess,valid,gameWord,correct):
        guess = guess.lower()
        if guess not in FIVE_LETTER_WORDS:
            valid = False
            gw.show_message("Not in word list")
        elif guess == gameWord:
            gw.show_message(f"You guessed the word in {gw.get_current_row()+1} guesses!")
            valid = True
            correct = True
        else:
            gw.show_message("So far, so good")
            valid = True
        return valid, correct

        
    def enter_action(s):
        row = gw.get_current_row()
        guess = ""
        valid = False
        correct = False
        for l in range(N_COLS):
            guess = guess + gw.get_square_letter(row,l)
        valid, correct = check_word(guess,valid,gameWord,correct)
        color_letters(guess)
        
    
        if valid == True:    
            row = row + 1

        row = gw.set_current_row(row)

        
    def color_letters(guess):
        alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        for l in guess:
            alphabet[l.lower()] += 1
        # if 3 in alphabet.values():
        #     #do something
        # elif 2 in alphabet.values():
        #     #do something
            
        

  
        
        
    
    gw = WordleGWindow()
    row = 0
    gw.add_enter_listener(enter_action)
    gw.set_current_row(row)
    print(gameWord)

    


    
    #Convert word to letters and place in first row
    # for x in range(0,N_COLS):
    #     gw.set_square_letter(0,x,word[x])


    

# Startup code

if __name__ == "__main__":
    wordle()
