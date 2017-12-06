#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student_fifteen.py
Created on Mon Nov 27 10:03:49 2017

@author: zachsills
"""
n = int(input("Please enter a value: "))

board = []

def make_board(n):
    """
    1. 'n' is an integer between 3 and 9.  
    2. Makes a board which is a list of n lists, each list representing a row in the board. 
    3. Assigns a value from the (n * n - 1) to 0 to each tile.  
    4. Prints out the board as a two dimensional array of values. 
    5. If n is even, the 2 and 1 tiles are swapped.
    """
    global board
    global max_value
    max_value = n * n # The number of tiles in the board
    count = 1 # A counter to change the value assigned to each tile
    for i in range(n):
        board.append([]) # Appends a list inside the list of board.  Essentially creates a row which is of type list.
        for j in range(n):
            num = max_value - count
            tile = '  ' if num == 0 else (' ' + (str(1 if num == 2 else 2 if num == 1 else num) if n % 2 == 0 else str(num)) if num < 10 else str(num))
            board[i].append(tile) # Appends a tile value to each row, n number of times.
            count += 1
    print_board(board)
        
def print_board(board):
    """
    Prints the board in a row by row sequence.
    """
    for row in board: print(' '.join(row)) # Prints the values in the row as a string separated by ' '.
            
def find_blank(board):
    """
    Takes the board as input and returns a tuple which contains the row and column location of the blank tile.
    """
    row, column = 0, 0
    for board_row in board:
        for string in board_row:
            if string == '  ':
                row, column = board.index(board_row), board_row.index(string)
                break
    return (row, column)

def find_tile(tile):
    """
    Tile is a string value that the user inputs.  
    The function returns a tuple which is the row and column values of the location of the tile on the board.
    """
    row, column = -1, -1
    for board_row in board:
        for string in board_row:
            if string.replace(' ', '') == tile:
                row, column = board.index(board_row), board_row.index(string)
                break
    return (row, column)

def next_to_blank(blank, tile):
    """
    Blank is a tuple of the row and column location of the blank tile.  
    Tile is a tuple containing the row and column location of the tile to be moved. 
    Only tiles adjacent to the blank tile can be moved.  
    The function returns True if the tile is adjacent to the blank tile and False if it is not.
    """
    hor_movement, vert_movement = abs(blank[0] - tile[0]), abs(blank[1] - tile[1])
    if vert_movement == 0 and hor_movement == 1:
        return True
    elif vert_movement == 1 and hor_movement == 0:
        return True
    return False


def update_tiles(blank, tile):
    """
    Blank is a tuple of the row and column location of the blank tile.  
    Tile is a tuple containing the row and column location of the tile to be moved. 
    Swaps the position of the blank tile and tile to be moved. 
    Prints the updated board after swap.
    """
    board[blank[0]][blank[1]], board[tile[0]][tile[1]] = board[tile[0]][tile[1]], '  '
    print_board(board)

def check_for_win(board):
    """
    Takes the board as input and checks to see if all the tiles are in order from least to greatest.  
    Returns False if they are not and True if board is complete.
    """
    previous_value = 1
    for row in board:
        for value in row:
            if value == '  ':
                continue
            current_value = value.replace(' ', '')
            if int(current_value) < int(previous_value):
                return False
            previous_value = current_value
    return True if board[len(board) - 1][len(board[len(board) - 1]) - 1] == '  ' else False

def valid_tile(tile):
    """
    Checks if the provided tile is a valid tile.
    Returns true if the tile is valid, otherwise, false.
    """
    if not tile.isdigit():
        return tile == 'stop'
    if abs(int(tile)) >= max_value:
        return False
    tile = find_tile(tile)
    if tile[0] == -1 and tile[1] == -1:
        return False
    return next_to_blank(find_blank(board), tile)

moves = 0
make_board(n)
while not check_for_win(board):
    tile = input('Please enter a value you wish to switch: ')
    while not valid_tile(tile):
        tile = input('Please enter a valid tile: ')
    if tile == 'stop':
        break
    update_tiles(find_blank(board), find_tile(tile))
    moves += 1
    
print('Congratulations! You won!')
print('Total moves:', moves)