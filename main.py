import sys
import pygame
from menu import main_menu, options_menu, difficulty_menu
from game import game_loop, game_win, game_over

MAX_LEVELS = 2

while True:
    choice = main_menu()
    if choice == 'play':
        difficulty = difficulty_menu()
        level = 1
        while level <= MAX_LEVELS:
            result = game_loop(difficulty, level)
            if result == 'next_level':
                level += 1
            elif result == 'game_over':
                game_over()
                break
            if level > MAX_LEVELS:
                game_win()
                break
                
    elif choice == 'options':
        options_menu()
