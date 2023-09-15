"""
Damn, that's wild.
I got not clue what I'm going to do with this but I'm gonna make something.
RPG Game?
"""

import random
import math

GLOBAL_board = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
                "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",]
    
def player():
    """
    Keep track of player level and stats
    """
    player_stats = [500, 100, 100, 50]
    


def movement():
    """
    Spawn monsters, players, and blockages
    """
    
    player_spawn_location = random(1, 70)
    GLOBAL_board[player_spawn_location] = "X"
    
    """
    Change player location based on movement
    """
    
    direction_of_movement = input("Left, Right, Up, Or Down? (Type WASD) : ")
    if direction_of_movement == "W":
        """
        Move up
        """
        if player_spawn_location <= 10:
            print("You cannot move any further upwards...\nPlease Choose Another Direction")
        else:
            player_current_location = player_spawn_location - 10    
            GLOBAL_board[player_current_location] = "X"
            GLOBAL_board[player_spawn_location] = "O"
        
    if direction_of_movement == "A":
        """
        Move left
        """
        if player_spawn_location == 1 or 11 or 21 or 31 or 41 or 51 or 61:
            print("You cannot move any further left...\nPlease Choose Another Direction")
        else:
            player_current_location = player_spawn_location - 1
            GLOBAL_board[player_current_location] = "X"
            GLOBAL_board[player_spawn_location] = "O"
        
    if direction_of_movement == "S":
        """
        Move down
        """
        if player_spawn_location >= 61:
            print("You cannot move any further downwards...\nPlease Choose Another Direction")
        else:
            player_current_location = player_spawn_location + 10
            GLOBAL_board[player_current_location] = "X"
            GLOBAL_board[player_spawn_location] = "O"
            
    if direction_of_movement == "D":
        """
        Move Right
        """
        if player_spawn_location == 10 or 20 or 30 or 40 or 50 or 60 or 70:
            print("You cannot move any further right...\nPlease Choose Another Direction")
        else:
            player_current_location = player_spawn_location + 1
            GLOBAL_board[player_current_location] = "X"
            GLOBAL_board[player_spawn_location] = "O"
            
