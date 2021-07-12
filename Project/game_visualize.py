"""Visualize a spectator game based on the type of bots being used.
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO"""

import pygame
import sys
import game_code
from typing import Any


pygame.init()
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load("assets/Backgrounds/world-of-warships-2019-t4-1280x720.jpg")
label_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 24)
message_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 48)
instruction_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 18)


def create_grid(player1: game_code.Player, player2: game_code.Player) -> None:
    """Create a PyGame grid"""
    status = True
    abort = False

    # Initialize two game board both with randomized ship placements
    player_1 = game_code.RandomizedBattleshipGame()
    player_2 = game_code.RandomizedBattleshipGame()

    player_1_sequence = []
    player_2_sequence = []
    player_1_previous_move = None
    player_2_previous_move = None

    save_initial_state1 = player_1
    save_initial_state2 = player_2

    escape = instruction_font.render('HIT ESC TO RETURN TO THE MAIN MENU OR TO START A NEW GAME', False,
                                     (255, 255, 255))
    player_label_1 = label_font.render('Player 1', False, (255, 255, 255))
    player_label_2 = label_font.render('Player 2', False, (255, 255, 255))

    while status:
        screen.blit(background, (0, 0))

        # Draw the grids belonging to each player
        for column in range(0, 8):
            for row in range(0, 8):
                cell = pygame.Rect((190 + column * 50, 160 + row * 50), (50, 50))
                pygame.draw.rect(screen, (255, 255, 255, 1), cell, 0)
                pygame.draw.rect(screen, (0, 0, 0, 1), cell, 3)

        for column in range(0, 8):
            for row in range(0, 8):
                cell = pygame.Rect((690 + column * 50, 160 + row * 50), (50, 50))
                pygame.draw.rect(screen, (255, 255, 255, 1), cell, 0)
                pygame.draw.rect(screen, (0, 0, 0, 1), cell, 3)

        # Display labels and text
        screen.blit(player_label_1, (340, 580))
        screen.blit(player_label_2, (840, 580))
        screen.blit(escape, (25, 685))

        columns = 'ABCDEFGH'
        rows = '12345678'
        # Label Player 1 Board
        for letter in range(0, 8):
            label = label_font.render(columns[letter], False, (255, 255, 255))
            screen.blit(label, (205 + letter * 50, 125))
        for number in range(0, 8):
            label = label_font.render(rows[number], False, (255, 255, 255))
            screen.blit(label, (165, 170 + number * 50))
        # Label Player 2 Board
        for letter in range(0, 8):
            label = label_font.render(columns[letter], False, (255, 255, 255))
            screen.blit(label, (705 + letter * 50, 125))
        for number in range(0, 8):
            label = label_font.render(rows[number], False, (255, 255, 255))
            screen.blit(label, (665, 170 + number * 50))

        # Display the ships prior to starting the game
        display_ships(save_initial_state1, True)
        display_ships(save_initial_state2, False)

        if player_1_previous_move is None and player_2_previous_move is None:
            pygame.display.update()
            pygame.time.wait(1000)

        while player_1.get_winner() is None and player_2.get_winner() is None and not abort:

            # player1 shot on player2 Board
            player_1_previous_move = player1.make_move(player_2, player_1_previous_move)
            player_2.make_move(player_1_previous_move)
            player_1_sequence.append(player_1_previous_move)
            if player_2.get_winner() is not None:
                break
            #  player1 on player2 Board
            player_2_previous_move = player2.make_move(player_1, player_2_previous_move)
            player_1.make_move(player_2_previous_move)
            player_2_sequence.append(player_2_previous_move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        abort = True
                        status = False

            display_ships(player_1, True)
            pygame.time.wait(500)
            pygame.display.update()
            pygame.time.wait(500)
            display_ships(player_2, False)
            pygame.display.update()

        # Display the victory message of the winning player
        if player_1.get_winner() == 'Lost':
            winner = 'Player 2'
            victory = message_font.render(winner + ' Wins!', False, (255, 255, 255))
            screen.blit(victory, (450, 50))
        else:
            winner = 'Player 1'
            victory = message_font.render(winner + ' Wins!', False, (255, 255, 255))
            screen.blit(victory, (450, 50))

        # Display the final state of the game
        display_ships(player_1, True)
        display_ships(player_2, False)

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False

        pygame.display.update()


letter_coordinates = {'A': (215, 715), 'B': (265, 765), 'C': (315, 815), 'D': (365, 865), 'E': (415, 915),
                      'F': (465, 965), 'G': (515, 1015), 'H': (565, 1065)}
number_to_coordinate = {'1': 185, '2': 235, '3': 285, '4': 335, '5': 385, '6': 435, '7': 485, '8': 535}

FILE_TO_INDEX = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
INDEX_TO_FILE = {i: f for f, i in FILE_TO_INDEX.items()}
RANK_TO_INDEX = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
INDEX_TO_RANK = {i: r for r, i in RANK_TO_INDEX.items()}


def algebraic_to_index(move: str) -> tuple[int, int]:
    """Convert coordinates in algebraic format ex. 'a2' to array indices (y, x)."""
    return (RANK_TO_INDEX[move[1]], FILE_TO_INDEX[move[0]])


def index_to_algebraic(pos: tuple[int, int]) -> str:
    """Convert coordinates in array indices (y, x) to algebraic format."""
    return INDEX_TO_FILE[pos[1]] + INDEX_TO_RANK[pos[0]]


def convert_letter_coord(player_1: bool, position: str) -> Any:
    """Convert a cell number into a coordinate
    Preconditions:
        -positions[1] in range(1, 9)
        -positions[0] in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
        -player_type == 'Player1' or player_type == 'Player2'
    """
    if player_1:
        x_axis = letter_coordinates.get(position[0])[0]
        y_axis = number_to_coordinate.get(position[1])
        return (x_axis, y_axis)

    else:
        x_axis = letter_coordinates.get(position[0])[1]
        y_axis = number_to_coordinate.get(position[1])
        return (x_axis, y_axis)


def display_ship(player_1: bool, position: str, kind: str) -> None:
    """Display a chunk of a ship based on its type"""
    hit = pygame.image.load("assets/Misc/x-mark-48.png")
    miss = pygame.image.load("assets/Misc/x-mark-48 (1).png")
    position = convert_letter_coord(player_1, position)
    if kind == 'Ca':
        pygame.draw.circle(screen, (0, 128, 255), position, 25)
    elif kind == 'B':
        pygame.draw.circle(screen, (157, 0, 255), position, 25)
    elif kind == 'Cr':
        pygame.draw.circle(screen, (0, 17, 255), position, 25)
    elif kind == 'S':
        pygame.draw.circle(screen, (100, 100, 100), position, 25)
    elif kind == 'D':
        pygame.draw.circle(screen, (25, 80, 30), position, 25)
    elif kind == 'M':
        screen.blit(miss, (position[0]-24, position[1]-24))
    else:
        screen.blit(hit, (position[0] - 24, position[1] - 24))


def display_ships(game: game_code.BattleshipGame, player_1: bool) -> None:
    """Display all the ships on the game board"""
    for cell_number in range(0, 8):
        for cell_letter in range(0, 8):
            piece = game.get_board()[cell_number][cell_letter]
            if piece is not None:
                cell = index_to_algebraic((cell_number, cell_letter))
                display_ship(player_1, cell, piece.kind)
