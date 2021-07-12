"""This file is the primary PyGame visualization file for our player game-mode. This file constitutes the code
used to visualize and interact with a user during a user-based battleship game.

NOTE: We are aware that PyCharm raises the mutation of the user_game_board as a problem. However after
reviewing our code and researching the problem we concluded that it is simply PyCharm making an incorrect assumption
and therefore falsely flagging the mutation based on the input type of the user_game_board as it is initialized to
only contain 'None' and therefore PyCharm believes that an input that is not None is invalid.

COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO
"""


import pygame
import sys
import game_code
import game_visualize
from typing import Tuple

# Initialize PyGame and global fonts
pygame.init()
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load("assets/Backgrounds/world-of-warships-2019-t4-1280x720.jpg")
label_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 24)
message_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 48)
instruction_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 18)

# Initialize the PyGame mixer
pygame.mixer.init()
click_sfx = pygame.mixer.Sound("assets/Music/Highlight.wav")
click_sfx.set_volume(0.5)

# Initialize a global user board that can be accessed and mutated throughout games
user_game_board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]

# Load the corresponding ship colors based on length (5, 4, 3, 3, 2)
ship_colours = [(0, 128, 255), (157, 0, 255), (0, 17, 255), (100, 100, 100), (25, 80, 30)]

# Initialize a global ships on board attribute
ships_on_board = 0

# Coordinates of the center of each cell (used for showing icons)
letter_coordinates = {'A': (215, 715), 'B': (265, 765), 'C': (315, 815), 'D': (365, 865), 'E': (415, 915),
                      'F': (465, 965), 'G': (515, 1015), 'H': (565, 1065)}
number_to_coordinate = {'1': 185, '2': 235, '3': 285, '4': 335, '5': 385, '6': 435, '7': 485, '8': 535}

# Conversion dictionaries from cell numbers to list indices
FILE_TO_INDEX = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
INDEX_TO_FILE = {i: f for f, i in FILE_TO_INDEX.items()}
RANK_TO_INDEX = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
INDEX_TO_RANK = {i: r for r, i in RANK_TO_INDEX.items()}

# Conversion Dictionary from mouse ranges to Cell letters
letter_cell_coordinates = {(range(190, 240), range(690, 740)): 'A', (range(240, 290), range(740, 790)): 'B',
                           (range(290, 340), range(790, 840)): 'C', (range(340, 390), range(840, 890)): 'D',
                           (range(390, 440), range(890, 940)): 'E', (range(440, 490), range(940, 990)): 'F',
                           (range(490, 540), range(990, 1040)): 'G', (range(540, 591), range(1040, 1091)): 'H'}

# Conversion Dictionary from mouse ranges to Cell numbers
number_cell_coordinates = {range(160, 210): '1', range(210, 260): '2', range(260, 310): '3',
                           range(310, 360): '4', range(360, 410): '5', range(410, 460): '6',
                           range(460, 510): '7', range(510, 561): '8'}

# A global attribute that keeps track on shots fire on by a user
user_sequence = []


def create_grid(ai_player: game_code.Player, sound: bool) -> None:
    """Create a user game mode PyGame grid and play a game"""
    status = True
    click = False
    orientation = True
    abort = False

    # Create the various display messages
    orientation_message = label_font.render('HIT SPACE TO CHANGE SHIP ORIENTATION', False,
                                            (255, 255, 255))
    click_message = label_font.render('LEFT CLICK TO PLACE A SHIP', False,
                                      (255, 255, 255))
    click_message_game = label_font.render('LEFT CLICK ON THE FIRING BOARD TO FIRE AT YOUR ENEMY', False,
                                           (255, 255, 255))

    # Track the previous move of each player
    user_previous_move = None
    ai_previous_move = None

    # Enable access to mutate the user game board, the amount of ships on board and the user's move sequence
    global user_game_board, ships_on_board, user_sequence

    # Initialize a battleship game using the user's current board
    user_board = game_code.RandomizedBattleshipGame(user_game_board)

    # Initialize a battleship game with a randomly generated ship board.
    ai_board = game_code.RandomizedBattleshipGame()

    # Update the screen until the user quits with the following
    while status:
        screen.blit(background, (0, 0))

        # Draw the grid of the user
        for column in range(0, 8):
            for row in range(0, 8):
                cell = pygame.Rect((190 + column * 50, 160 + row * 50), (50, 50))
                pygame.draw.rect(screen, (255, 255, 255, 1), cell, 0)
                pygame.draw.rect(screen, (0, 0, 0, 1), cell, 3)

        # Draw the firing board
        for column in range(0, 8):
            for row in range(0, 8):
                cell = pygame.Rect((690 + column * 50, 160 + row * 50), (50, 50))
                pygame.draw.rect(screen, (255, 255, 255, 1), cell, 0)
                pygame.draw.rect(screen, (0, 0, 0, 1), cell, 3)

        # Display the labels of each grid
        display_grid_labels()

        # Wait for the first ship to be placed
        if ships_on_board == 0:
            screen.blit(orientation_message, (400, 60))
            screen.blit(click_message, (475, 10))
            display_ship_placement(click, 5, orientation, ship_colours[0], 'Ca')
            game_visualize.display_ships(user_board, True)
        # Wait for the second ship to be placed
        elif ships_on_board == 1:
            screen.blit(orientation_message, (400, 60))
            screen.blit(click_message, (475, 10))
            display_ship_placement(click, 4, orientation, ship_colours[1], 'B')
            game_visualize.display_ships(user_board, True)
        # Wait for the third ship to be placed
        elif ships_on_board == 2:
            screen.blit(orientation_message, (400, 60))
            screen.blit(click_message, (475, 10))
            display_ship_placement(click, 3, orientation, ship_colours[2], 'Cr')
            game_visualize.display_ships(user_board, True)
        # Wait for the fourth ship to be placed
        elif ships_on_board == 3:
            screen.blit(orientation_message, (400, 60))
            screen.blit(click_message, (475, 10))
            display_ship_placement(click, 3, orientation, ship_colours[3], 'S')
            game_visualize.display_ships(user_board, True)
        # Wait for the fifth ship to be placed
        elif ships_on_board == 4:
            screen.blit(orientation_message, (400, 60))
            screen.blit(click_message, (475, 10))
            display_ship_placement(click, 2, orientation, ship_colours[4], 'D')
            game_visualize.display_ships(user_board, True)
        # If all ships have been placed, run a game
        else:
            # Display the pre-firing state of the game board
            game_visualize.display_ships(user_board, True)
            display_ships_hidden(ai_board, False)

            while user_board.get_winner() is None and ai_board.get_winner() is None and not abort:
                screen.blit(click_message_game, (300, 10))
                # Player's shot on AI board
                pygame.display.update()
                while user_previous_move is None:
                    # Wait for a user to make a move by clicking
                    user_previous_move = user_move(click)
                    click = False

                    # Check if the user wants to leave the game or is clicking
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                if sound:
                    click_sfx.play()

                # AI makes a move
                ai_board.make_move(user_previous_move)
                user_sequence.append(user_previous_move)
                user_previous_move = None
                ai_previous_move = ai_player.make_move(user_board, ai_previous_move)
                user_board.make_move(ai_previous_move)

                # Update the two boards with a 1 second delay
                display_ships_hidden(ai_board, False)
                pygame.display.update()
                pygame.time.wait(1000)
                game_visualize.display_ships(user_board, True)
                pygame.display.update()

                # Check for user input. If the user wants to quit the game reset their board,
                # sequence and ship shot count
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            user_game_board = [
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None],
                                [None, None, None, None, None, None, None, None]
                            ]
                            ships_on_board = 0
                            user_sequence = []
                            abort = True
                            status = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

        # Display a victory message for the appropriate player
        if ai_board.get_winner() == 'Lost':
            winner = 'You'
            victory = message_font.render(winner + ' Win!', False, (255, 255, 255))
            screen.blit(victory, (510, 50))
        elif user_board.get_winner() == 'Lost':
            winner = 'The AI Player'
            victory = message_font.render(winner + ' Wins!', False, (255, 255, 255))
            screen.blit(victory, (410, 50))

        # Display the final state of the game
        game_visualize.display_ships(user_board, True)
        display_ships_hidden(ai_board, False)

        click = False

        display_grid_labels()

        # Check for user input. If the user wants to quit the game reset their board, sequence and ship shot count
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    user_game_board = [
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None]
                    ]
                    ships_on_board = 0
                    user_sequence = []
                    status = False
                if event.key == pygame.K_SPACE:
                    orientation = not orientation
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def display_grid_labels() -> None:
    """Display the labels of each grid on the PyGame Screen"""
    board1_label = label_font.render('Ship Board', False, (255, 255, 255))
    board2_label = label_font.render('Firing Board', False, (255, 255, 255))
    escape = instruction_font.render('HIT ESC TO RETURN TO THE MAIN MENU OR TO RESET THE GAME', False,
                                     (255, 255, 255))

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

    screen.blit(board1_label, (320, 580))
    screen.blit(board2_label, (800, 580))
    screen.blit(escape, (25, 685))


def check_valid(cell: str) -> bool:
    """Check if the values at the corresponding list indices are valid moves"""
    global user_sequence
    return cell not in user_sequence


def user_move(click: bool) -> str:
    """Register a user's click on the firing board
        as a move in the system"""
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Make sure the mouse is withing the boundaries of the firing board
    if 690 <= mouse_x <= 1090 and 160 <= mouse_y <= 560:
        cell = convert_mouse_to_letternum(mouse_x, mouse_y, False)
        if click and check_valid(cell):
            return cell


def convert_mouse_to_letternum(mouse_x: int, mouse_y: int, placements: bool) -> str:
    """Convert a mouse coordinate into the cell center where placements
    determines which of the two grids it should convert it to."""
    letter = None
    number = None
    for h_cell in letter_cell_coordinates:
        if placements:
            if mouse_x in h_cell[0]:
                letter = letter_cell_coordinates[h_cell]
        else:
            if mouse_x in h_cell[1]:
                letter = letter_cell_coordinates[h_cell]
    for v_cell in number_cell_coordinates:
        if mouse_y in v_cell:
            number = number_cell_coordinates[v_cell]
    return letter + number


def convert_mouse_to_display_pos(mouse_x: int, mouse_y: int, placements: bool) -> Tuple[int, int]:
    """Convert a mouse coordinate into the cell center"""
    conversion = convert_mouse_to_letternum(mouse_x, mouse_y, placements)
    return game_visualize.convert_letter_coord(placements, conversion)


def display_piece(player_1: bool, position: str, kind: str) -> None:
    """Display a hit or a miss"""
    hit = pygame.image.load("assets/Misc/x-mark-48.png")
    miss = pygame.image.load("assets/Misc/x-mark-48 (1).png")
    position = game_visualize.convert_letter_coord(player_1, position)
    if kind == 'M':
        screen.blit(miss, (position[0] - 24, position[1] - 24))
    elif kind == 'H':
        screen.blit(hit, (position[0] - 24, position[1] - 24))


def display_ships_hidden(game: game_code.BattleshipGame, player_1: bool) -> None:
    """Display all the ships on the game board"""
    for cell_number in range(0, 8):
        for cell_letter in range(0, 8):
            piece = game.get_board()[cell_number][cell_letter]
            if piece is not None:
                cell = game_visualize.index_to_algebraic((cell_number, cell_letter))
                display_piece(player_1, cell, piece.kind)


def display_ship_placement(click: bool, length: int, orientation: bool, color: Tuple[int, int, int],
                           ship_type: str) -> None:
    """Display the ship based on the user's mouse taking into account that a user's mouse might not be on the grid.
    In which case the ship is displayed the farthest it can possibly be displayed on the grid
    While the amount of lines may look intimidating, there are simply a lot of possibilities when the user mouse is
    past the right position. Each chunk pretty much does the same thing: Display a ship in the right cells."""

    mouse_x, mouse_y = pygame.mouse.get_pos()
    global user_game_board, ships_on_board
    # check mouse position based on a horizontal ship orientation
    if orientation:
        # check if the mouse position is within the grid and withing the length of the ship
        if 190 <= mouse_x <= 189 + (9 - length) * 50 and 160 <= mouse_y <= 560:
            pos = convert_mouse_to_display_pos(mouse_x, mouse_y, True)
            cell = convert_mouse_to_letternum(mouse_x, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the top left corner of the grid
        if mouse_y < 160 and mouse_x < 190:
            pos = convert_mouse_to_display_pos(200, 170, True)
            cell = convert_mouse_to_letternum(200, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the bottom left corner of the grid
        if mouse_y > 560 and mouse_x < 190:
            pos = convert_mouse_to_display_pos(200, 550, True)
            cell = convert_mouse_to_letternum(200, 550, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the bottom right boundary for the ship length
        if mouse_y > 560 and mouse_x > 189 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(189 + (9 - length) * 50, 540, True)
            cell = convert_mouse_to_letternum(189 + (9 - length) * 50, 540, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the top right boundary for the ship length
        if mouse_y < 160 and mouse_x > 189 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(189 + (9 - length) * 50, 170, True)
            cell = convert_mouse_to_letternum(189 + (9 - length) * 50, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the top boundary
        if 190 <= mouse_x <= 189 + (9 - length) * 50 and mouse_y < 160:
            pos = convert_mouse_to_display_pos(mouse_x, 170, True)
            cell = convert_mouse_to_letternum(mouse_x, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the bottom boundary
        if 190 <= mouse_x <= 189 + (9 - length) * 50 and mouse_y > 560:
            pos = convert_mouse_to_display_pos(mouse_x, 540, True)
            cell = convert_mouse_to_letternum(mouse_x, 540, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the far right boundary based on ship length
        if mouse_x > 189 + (9 - length) * 50 and 160 <= mouse_y <= 560:
            pos = convert_mouse_to_display_pos(189 + (9 - length) * 50, mouse_y, True)
            cell = convert_mouse_to_letternum(189 + (9 - length) * 50, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the far left boundary
        if mouse_x < 190 and 160 <= mouse_y <= 560:
            pos = convert_mouse_to_display_pos(200, mouse_y, True)
            cell = convert_mouse_to_letternum(200, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0] + i * 50, pos[1]), 25)
                check_all.append(user_game_board[y][x + i] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None
    # Check the boundaries if the ship is in the vertical position
    else:
        # check if the mouse is within the grid boundaries for a vertical ship
        if 190 <= mouse_x <= 590 and 160 <= mouse_y <= 159 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(mouse_x, mouse_y, True)
            cell = convert_mouse_to_letternum(mouse_x, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None
        # check if the mouse is past the top left corner of the grid
        if mouse_y < 160 and mouse_x < 190:
            pos = convert_mouse_to_display_pos(200, 170, True)
            cell = convert_mouse_to_letternum(200, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the bottom left corner of the grid based on ship length
        if mouse_y > 160 + (9 - length) * 50 and mouse_x < 190:
            pos = convert_mouse_to_display_pos(200, 159 + (9 - length) * 50, True)
            cell = convert_mouse_to_letternum(200, 159 + (9 - length) * 50, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x + index] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the bottom right corner of the grid based on ship length
        if mouse_y > 160 + (9 - length) * 50 and mouse_x > 590:
            pos = convert_mouse_to_display_pos(580, 159 + (9 - length) * 50, True)
            cell = convert_mouse_to_letternum(580, 159 + (9 - length) * 50, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the top right corner of the grid
        if mouse_y < 160 and mouse_x > 590:
            pos = convert_mouse_to_display_pos(580, 170, True)
            cell = convert_mouse_to_letternum(580, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the top of the grid
        if 190 <= mouse_x <= 590 and mouse_y < 160:
            pos = convert_mouse_to_display_pos(mouse_x, 170, True)
            cell = convert_mouse_to_letternum(mouse_x, 170, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
                if click and all(check_all):
                    for index in range(0, length):
                        user_game_board[y + index][x] = game_code.Piece(ship_type)
                    ships_on_board += 1
                    return None

        # check if the mouse is past the bottom of the grid based on ship length
        if 190 <= mouse_x <= 590 and mouse_y > 160 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(mouse_x, 158 + (9 - length) * 50, True)
            cell = convert_mouse_to_letternum(mouse_x, 158 + (9 - length) * 50, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the right side of the grid
        if mouse_x > 590 and 160 <= mouse_y <= 159 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(580, mouse_y, True)
            cell = convert_mouse_to_letternum(580, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + i][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None

        # check if the mouse is past the left side of the grid
        if mouse_x < 190 and 160 <= mouse_y <= 160 + (9 - length) * 50:
            pos = convert_mouse_to_display_pos(200, mouse_y, True)
            cell = convert_mouse_to_letternum(200, mouse_y, True)
            y, x = game_visualize.algebraic_to_index(cell)
            check_all = []
            for i in range(0, length):
                pygame.draw.circle(screen, color, (pos[0], pos[1] + i * 50), 25)
                check_all.append(user_game_board[y + 1][x] is None)
            if click and all(check_all):
                for index in range(0, length):
                    user_game_board[y + index][x] = game_code.Piece(ship_type)
                ships_on_board += 1
                return None
