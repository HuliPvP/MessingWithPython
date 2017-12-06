#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps3_hangman.py
Created on Wed Dec  6 09:54:26 2017

@author: thesills
"""
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordList = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    finalString = ''
    for letter in secretWord:
        finalString += '_' if letter not in lettersGuessed else letter
    return finalString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphaList = list('abcdefghijklmnopqrstuvwxyz')
    for letter in lettersGuessed: alphaList.remove(letter)
    return alphaList

def validInput(guess):
    return True if ((guess in getAvailableLetters(lettersGuessed)) or (guess == 'stop')) else False

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    global roundCount
    guess = input('Your letter guess: ').lower()
    while guess.isdigit() or len(guess) != 1:
        guess = input('Your letter guess: ').lower()
    if guess == 'stop': return 'stop'
    if guess not in secretWord or guess not in getAvailableLetters(lettersGuessed):
        if guess not in lettersGuessed: lettersGuessed.append(guess)
        roundCount += 1
        if roundCount != 8: print('Guesses left: ', 8 - roundCount)
    else:
        lettersGuessed.append(guess)
        guess = 'win' if isWordGuessed(secretWord, lettersGuessed) else guess
    if roundCount != 8: print(getGuessedWord(secretWord, lettersGuessed))
    return guess


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

lettersGuessed = []
secretWord = chooseWord(wordList).lower()
print('Secret word: ', secretWord)
print('Welcome to the game Hangman!')
print('I am thinking of a word that is', len(secretWord), 'letters long.')
print(getGuessedWord(secretWord, lettersGuessed))
while roundCount != 8:
    result = hangman(secretWord)
    if result == 'stop' or result == 'win':
        break

print('Congratulations, you guessed the word!' if roundCount != 8 else 'Sorry, you ran out of guesses!\nThe word was: ' + secretWord)
roundCount = 0