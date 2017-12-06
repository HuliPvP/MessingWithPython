#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dictionaries_day_3.py
Created on Tue Dec  5 09:38:36 2017

@author: thesills
"""
def word0(array):
    dictionary = {}
    for i in array: dictionary.setdefault(i, 0)
    return dictionary

print(word0(["a", "b", "a", "b"]))
print(word0(["a", "b", "a", "c", "b"]))
print(word0(["c", "b", "a"]))

def wordLen(array):
    dictionary = {}
    for i in array: dictionary.setdefault(i, len(i))
    return dictionary

print(wordLen(["a", "bb", "a", "bb"]))
print(wordLen(["this", "and", "that", "and"]))
print(wordLen(["code", "code", "code", "bug"]))

def pairs(array):
    dictionary = {}
    for i in array: dictionary.setdefault(i[0], i[-1])
    return dictionary

print(pairs(["code", "bug"]))
print(pairs(["man", "moon", "main"]))
print(pairs(["man", "moon", "good", "night"]))

def wordCount(array):
    dictionary = {}
    for i in array: dictionary.setdefault(i, array.count(i))
    return dictionary

print(wordCount(["a", "b", "a", "c", "b"]))
print(wordCount(["c", "b", "a"]))
print(wordCount(["c", "c", "c", "c"]))

def firstChar(array):
    dictionary = {}
    for i in array: dictionary.setdefault(i[0], 'placeholder')
    for key in dictionary.keys():
        final_string = ''
        for i in array:
            if i[0] == key: final_string += i
        dictionary[key] = final_string
    return dictionary

print(firstChar(["salt", "tea", "soda", "toast"]))
print(firstChar(["aa", "bb", "cc", "aAA", "cCC", "d"]))
print(firstChar([]))

def wordAppend(array):
    skip = []
    final_string = ''
    for i in array: 
        if array.count(i) % 2 == 0 and i not in skip:
            skip.append(i)
            for j in range(array.count(i) // 2):
                final_string += i
    return final_string

print(wordAppend(["a", "b", "a"]))
print(wordAppend(["a", "b", "a", "c", "a", "d", "a"]))
print(wordAppend(["a", "", "a"]))