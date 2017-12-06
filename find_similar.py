#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
find_similar.py
Created on Tue Nov 14 09:55:47 2017

@author: thesills
"""
locations = ['center', 'midright', 'midleft', 'topmid', 'topleft', 'lowleft', 'lowmid', 'lowright', 'topright']

def get_difference(a, b):
    distance = [0] * (len(a) + 1)
    for i in range(len(a) + 1):
        distance[i] = [0] * (len(b) + 1)
    for i in range(len(a) + 1):
        distance[i][0] = i
    for j in range(len(b) + 1):
        distance[0][j] = j
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            distance[i][j] = min(min(distance[i - 1][j] + 1, distance[i][j - 1] + 1), distance[i - 1][j - 1] + (0 if a[i -1] == b[j - 1] else 1))
    return distance[len(a)][len(b)]

def find_similar(to):
    chosen_word = ''
    difference = 10
    for word in locations:
        word_difference = get_difference(word, to)
        if word_difference < difference:
            difference = word_difference
            chosen_word = word
    return chosen_word

print('Did you mean?', find_similar('midtop'))