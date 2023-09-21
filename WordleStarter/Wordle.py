# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter as tk
from tkinter import Button


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import  WordleSquare, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, CORRECT_COLOR2, PRESENT_COLOR2
from WordleGraphics import WordleKey

def start_new_game():
    # Code to start a new game goes here
    pass


def wordle():
    
    def guess_counts(guess):
        guessDict = {}
        guess = guess.lower()
        for l in guess:
            if l in guessDict.keys():
                guessDict[l] += 1
            else:
                guessDict[l] = 1
        return guessDict

    def word_counts(gameWord):
        wordDict = {}
        gameWord = gameWord.lower()
        for l in gameWord:
            if l in wordDict.keys():
                wordDict[l] += 1
            else:
                wordDict[l] = 1
        return wordDict
    
    #Select Word
    def generateWord():
        gameWord = random.choice(FIVE_LETTER_WORDS)
        return gameWord
    
    gameWord = generateWord()
    print(gameWord)      
    

        #Check if word is valid
    def check_word(guess,valid,gameWord,correct):
        guess = guess.lower()
        wordDict = word_counts(gameWord)
        if guess not in FIVE_LETTER_WORDS:
            valid = False
            gw.show_message("Not in word list")
        elif guess == gameWord:
            for i in range(N_COLS):
                wordRow = gw.get_current_row()
                gw.set_square_color(wordRow, i, CORRECT_COLOR)
            gw.show_message(f"You guessed the word in {gw.get_current_row()+1} guesses!")
            valid = True
            correct = True
        else:
            guessDict = guess_counts(guess)
            for i in range(N_COLS):
                letter = guess[i]
                wordRow = gw.get_current_row()
                ws = WordleSquare(gw._canvas, wordRow, i)
                l = ws.get_letter()
                print(letter, l)
                

                if letter == gameWord[i]:
                    print("yes")
                    gw.set_square_color(wordRow, i, CORRECT_COLOR)
                    wordDict[letter] -= 1

                elif letter in gameWord:
                    if wordDict[letter] > 0:
                        print("maybe")
                        gw.set_square_color(wordRow, i, PRESENT_COLOR)
                        wordDict[letter] -= 1
                    else:
                        print("no")
                        gw.set_square_color(wordRow, i, MISSING_COLOR)
                else:
                    print("no")
                    gw.set_square_color(wordRow, i, MISSING_COLOR)

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

    
        if valid == True:    
            row = row + 1

        row = gw.set_current_row(row)

        
        
        
    
    gw = WordleGWindow()
    row = 0
    gw.add_enter_listener(enter_action)
    gw.set_current_row(row)
    
    
    english_button = Button(gw._canvas, text="English", command=start_new_game)
    english_button.place(x=10, y=10)  # Adjust x and y coordinates as needed

    somoli_button = Button(gw._canvas, text="Somoli", command=start_new_game)
    somoli_button.place(x=10, y=40)  # Adjust x and y coordinates as needed

    color_button = Button(gw._canvas, text="Standard", command=start_new_game)
    color_button.place(x=435, y=10)  # Adjust x and y coordinates as needed

    new_color_button = Button(gw._canvas, text="New Color", command=start_new_game)
    new_color_button.place(x=426, y=40)  # Adjust x and y coordinates as needed

    #Convert word to letters and place in first row
    # for x in range(0,N_COLS):
    #     gw.set_square_letter(0,x,word[x])


    

# Startup code

if __name__ == "__main__":
    wordle()
