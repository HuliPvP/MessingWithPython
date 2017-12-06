#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
longest_string_new.py
My second attempt at the longest substring problem set
Created on Mon Oct  2 15:33:04 2017

@author: zachsills
"""
s = input('Please type in a string here: ')

def get_longest_string(string):
    longest_string = ''
    for i in range(len(string)):
        for j in range(i, len(s) + 1):
            test_string = string[i:j]
            new_string = ''.join(sorted(test_string))
            if new_string == test_string:
                if len(new_string) > len(longest_string):
                    longest_string = new_string
    return longest_string

longest_string = get_longest_string(s)
print('Longest substring in alphabetical order is:', longest_string)