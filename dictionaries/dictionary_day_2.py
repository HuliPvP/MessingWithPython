#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dictionary_day_2.py
Created on Mon Dec  4 10:05:39 2017

@author: thesills
"""

def dictionaryShare(dictionary):
    if 'c' in dictionary:
        del dictionary['c']
        
    if 'a' in dictionary:
        dictionary['b'] = dictionary['a'] if 'b' in dictionary else dictionary.setdefault('b', dictionary['a'])
        
    return dictionary

print(dictionaryShare({"a": "aaa", "b": "bbb", "c": "ccc"}))
print(dictionaryShare({"b": "xyz", "c": "ccc"}))
print(dictionaryShare({"a": "aaa", "c": "meh", "d": "hi"}))

def dictionaryBully(dictionary):
    if 'a' in dictionary:
        dictionary['a'], dictionary['b'] = '', dictionary['a']
        
    return dictionary

print(dictionaryBully({"a": "candy", "b": "dirt"}))
print(dictionaryBully({"a": "candy"}))
print(dictionaryBully({"a": "candy", "b": "carrot", "c": "meh"}))

def dictionaryAB(dictionary):
    if 'a' in dictionary and 'b' in dictionary:
        dictionary.setdefault('ab', dictionary['a'] + dictionary['b'])
    
    return dictionary

print(dictionaryAB({"a": "Hi", "b": "There"}))
print(dictionaryAB({"a": "Hi"}))
print(dictionaryAB({"b": "There"}))


def topping2(dictionary):
    if 'ice cream' in dictionary:
        dictionary.setdefault('yogurt', dictionary['ice cream'])
        
    if 'spinach' in dictionary:
        dictionary['spinach'] = 'nuts'

    return dictionary

print(topping2({"ice cream": "cherry"}))
print(topping2({"spinach": "dirt", "ice cream": "cherry"}))
print(topping2({"yogurt": "salt"}))


def topping3(dictionary):
    if 'potato' in dictionary:
        dictionary.setdefault('fries', dictionary['potato'])
    
    if 'salad' in dictionary:
        dictionary.setdefault('spinach', dictionary['salad'])
        
    return dictionary

print(topping3({"potato": "ketchup"}))
print(topping3({"potato": "butter"}))
print(topping3({"salad": "oil", "potato": "ketchup"}))