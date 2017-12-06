#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ceasar_cipher.py
Created on Thu Oct 19 11:01:31 2017

@author: thesills
"""
def caesar(string, key):
    final_string = ''
    for c in string:
        char = c 
        if ord(c) in range(97, 123) or ord(c) in range(65, 91):
            char = chr(correct_ord(ord(c), key))
        final_string += char
    return final_string

def correct_ord(ordinal, key):
    lower_range = range(97, 123)
    higher_range = range(65, 91)
    if ordinal in lower_range and ordinal + key in lower_range:
        return ordinal + key
    elif ordinal in higher_range and ordinal + key in higher_range:
        return ordinal + key
    elif ordinal in lower_range or ordinal in higher_range:
        return (ordinal + key) - 26
    return ordinal
    

print(caesar('Be sure to drink your Ovaltine!', 13))