#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mario.py
Created on Wed Sep 27 10:08:32 2017

@author: thesills
"""
def is_valid_int(string):
    try: 
        int(string)
        if int(string) > 25 or int(string) < 0:
            return False
        return True
    except:
        return False

userInput = input('Height: ')
while not is_valid_int(userInput):
    userInput = input('Retry: ')

height = int(userInput)

def print_pyramid(size):
    current_amount = 1
    for i in range(size):
        current_string = ''
        current_string += (' ' * (size - current_amount)) + ('#' * (i + 1)) + ' ' + ('#' * (i + 1))
        current_amount += 1
        print(current_string)

print_pyramid(height)