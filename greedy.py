#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
greedy.py
Created on Tue Sep 19 09:41:21 2017

@author: thesills
"""
# Checks if the given parameter in the method is a float value and less than zero
# @param value - A float value
def is_float(value):
    try:
        float(value)
        return True if (float(value) > 0) else False
    except:
        return False

# Takes in the user input and stores the value in memory with the variable name of 'change'
change = input('O hai! How much change is owed? ')
# Repeatedly checks if the input provided by the user can be casted to a float value
# If not, if will keep asking for the input
while not is_float(change):
    change = input('How much change is owed? ')
# Once the check is successfully true, we can finally cast the input string to a float
change = round(float(change), 2)

# Declares and then initializes a list of all of the coin values we will be using for this problem set
coins = {0.25, 0.10, 0.05, 0.01}

# Defines a method to be able to get the amount of coins
# @param value - A float value
# @param values - A list of float values
def get_coins(value, values):
    totalValue = 0 # Defines a total 
    totalCoins = 0
    # Loops through every single value in the list of values provided as a parameter
    # and makes the current value equal to i
    for i in values:
        # Constantly checks if the value provided is less than the current value that is greater
        # or equal to the current value of i
        while value >= i:
            value = round(value - i, 2)
            totalValue += i
            totalCoins += 1
        if (totalValue == value): # Checks if the totalValue is now equal to the provided value
            break                 # Finally break the loop so we can now call the return method
    return totalCoins

# Calls the method get_coins(value, values) so we can store the proper amount of coins so
# we can use it later on in the code
# We also need to sort the list in descending order so that it checks each greater value first
total = get_coins(change, sorted(coins, reverse=True))
# Outputs the amount of coins that equal up to the amount of the float change
# Also there is a grammatical check so that others wouldn't call you out for being bad at English
print('You will need %d coin' %total + ('s.' if total > 1 else '.'))