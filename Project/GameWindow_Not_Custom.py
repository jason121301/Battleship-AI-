"""This file is the primary PyGame visualization file for our spectator game-mode."""


import pygame
import sys
import game_visualize
import game_code
import player
import algorithm_learning
import game_tree

# Initialize PyGame
pygame.init()
# Initialize a screen
screen = pygame.display.set_mode((1280, 720))
logo = pygame.image.load("assets/Misc/UofT_logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Battleship")
background = pygame.image.load("assets/Backgrounds/world-of-warships-2019-t4-1280x720.jpg")

pygame.mixer.init()
menu_music = pygame.mixer.Sound("assets/Music/Ready To Fight.mp3")
menu_music.set_volume(0.4)
menu_music.play(loops=-1)

click_sfx = pygame.mixer.Sound("assets/Music/Highlight.wav")
click_sfx.set_volume(0.5)


# Initialize Global Assets
music_on = True
sfx_on = True
a1_status = 'Easy'
a2_status = 'Easy'
pygame.font.init()


def main_menu() -> None:
    """Display the main menu of the game"""
    status = True
    click = False
    title_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 148)
    button_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 28)

    while status:
        screen.blit(background, (0, 0))

        title = title_font.render('BATTLESHIP', False, (255, 255, 255))
        screen.blit(title, (225, 5))
        # Initialize the button dimensions
        button_1 = pygame.Rect((540.0, 300.0), (200.0, 60.0))
        button_2 = pygame.Rect((540.0, 400.0), (200.0, 60.0))
        button_3 = pygame.Rect((540.0, 500.0), (200.0, 60.0))
        play_button = button_font.render('play', False, (255, 255, 255))
        spectate_button = button_font.render('spectate', False, (255, 255, 255))
        options_button = button_font.render('options', False, (255, 255, 255))

        # Draw the button body
        pygame.draw.rect(screen, (23, 113, 164, 1), button_1, 0, 8)
        pygame.draw.rect(screen, (23, 113, 164, 1), button_2, 0, 8)
        pygame.draw.rect(screen, (23, 113, 164, 1), button_3, 0, 8)
        screen.blit(play_button, (605, 310))
        screen.blit(spectate_button, (568, 410))
        screen.blit(options_button, (575, 510))

        # Draw the button outline
        pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
        pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
        pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 540 <= mouse_x <= 740 and 300 <= mouse_y <= 360:
            # Highlight the button under the cursor
            pygame.draw.rect(screen, (77, 175, 230, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            screen.blit(play_button, (605, 310))
            if click:
                if sfx_on:
                    click_sfx.play()
                play()

        if 540 <= mouse_x <= 740 and 400 <= mouse_y <= 460:
            # Highlight the button under the cursor
            pygame.draw.rect(screen, (77, 175, 230, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            screen.blit(spectate_button, (568, 410))
            if click:
                if sfx_on:
                    click_sfx.play()
                spectate()

        if 540 <= mouse_x <= 740 and 500 <= mouse_y <= 560:
            # Highlight the button under the cursor
            pygame.draw.rect(screen, (77, 175, 230, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(options_button, (575, 510))
            if click:
                if sfx_on:
                    click_sfx.play()
                options()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


def options() -> None:
    """Display the options page of the game"""
    status = True
    click = False
    title_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 124)
    options_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 48)
    button_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 24)
    instruction_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 18)

    while status:
        global music_on, sfx_on

        # Initialize Text
        screen.blit(background, (0, 0))
        title = title_font.render('options', False, (255, 255, 255))
        screen.blit(title, (350, 5))
        music = options_font.render('music', False, (255, 255, 255))
        screen.blit(music, (562, 225))
        sfx = options_font.render('sfx', False, (255, 255, 255))
        screen.blit(sfx, (592, 375))

        on = button_font.render('on', False, (255, 255, 255))
        off = button_font.render('off', False, (255, 255, 255))

        escape = instruction_font.render('HIT ESC TO RETURN TO THE MAIN MENU', False, (255, 255, 255))

        # Define button positions
        button_on_m = pygame.Rect((530.0, 300.0), (100.0, 60.0))
        button_off_m = pygame.Rect((650.0, 300.0), (100.0, 60.0))
        button_on_sfx = pygame.Rect((530.0, 450.0), (100.0, 60.0))
        button_off_sfx = pygame.Rect((650.0, 450.0), (100.0, 60.0))

        screen.blit(escape, (25, 685))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 530 <= mouse_x <= 630 and 300 <= mouse_y <= 360 and click:
            if sfx_on:
                click_sfx.play()
            music_on = False
            menu_music.stop()

        if 650 <= mouse_x <= 750 and 300 <= mouse_y <= 360 and click:
            if sfx_on:
                click_sfx.play()
            music_on = True
            menu_music.play()

        if 530 <= mouse_x <= 630 and 450 <= mouse_y <= 510 and click:
            if sfx_on:
                click_sfx.play()
            sfx_on = False

        if 650 <= mouse_x <= 750 and 450 <= mouse_y <= 510 and click:
            if sfx_on:
                click_sfx.play()
            sfx_on = True

        click = False

        # Display the appropriate button state
        if music_on:
            pygame.draw.rect(screen, (23, 113, 164, 1), button_on_m, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_on_m, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_off_m, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_off_m, 5, 8)
            screen.blit(on, (680, 315))
            screen.blit(off, (557, 315))

        if sfx_on:
            pygame.draw.rect(screen, (23, 113, 164, 1), button_on_sfx, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_on_sfx, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_off_sfx, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_off_sfx, 5, 8)
            screen.blit(on, (680, 465))
            screen.blit(off, (557, 465))

        if not sfx_on:
            pygame.draw.rect(screen, (23, 113, 164, 1), button_off_sfx, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_off_sfx, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_on_sfx, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_on_sfx, 5, 8)
            screen.blit(on, (680, 465))
            screen.blit(off, (557, 465))

        if not music_on:
            pygame.draw.rect(screen, (23, 113, 164, 1), button_off_m, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_off_m, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_on_m, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_on_m, 5, 8)
            screen.blit(on, (680, 315))
            screen.blit(off, (557, 315))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def spectate() -> None:
    """Display the spectator game-mode menu"""
    status = True
    click = False
    title_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 100)
    options_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 24)
    instruction_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 18)

    while status:
        global a1_status, a2_status
        screen.blit(background, (0, 0))
        title = title_font.render('SPECTATOR MODE', False, (255, 255, 255))
        screen.blit(title, (145, 5))

        escape = instruction_font.render('HIT ESC TO RETURN TO THE MAIN MENU', False, (255, 255, 255))
        screen.blit(escape, (25, 685))

        ai_1_text = options_font.render('Select AI 1 Difficulty', False, (255, 255, 255))
        screen.blit(ai_1_text, (170, 200))

        ai_2_text = options_font.render('Select AI 2 Difficulty', False, (255, 255, 255))
        screen.blit(ai_2_text, (770, 200))

        # Initialize the button dimensions
        button_1 = pygame.Rect((215.0, 250.0), (200.0, 60.0))
        button_2 = pygame.Rect((215.0, 330.0), (200.0, 60.0))
        button_3 = pygame.Rect((215.0, 410.0), (200.0, 60.0))
        button_4 = pygame.Rect((815.0, 250.0), (200.0, 60.0))
        button_5 = pygame.Rect((815.0, 330.0), (200.0, 60.0))
        button_6 = pygame.Rect((815.0, 410.0), (200.0, 60.0))

        start_button = pygame.Rect((465.0, 500.0), (300.0, 80.0))

        easy = options_font.render('Easy', False, (255, 255, 255))
        intermediate = options_font.render('Intermediate', False, (255, 255, 255))
        hard = options_font.render('Hard', False, (255, 255, 255))
        start_game = options_font.render('Start Game', False, (255, 255, 255))

        pygame.draw.rect(screen, (200, 0, 0, 1), start_button, 0, 8)
        pygame.draw.rect(screen, (0, 0, 0, 1), start_button, 5, 8)
        screen.blit(start_game, (535, 525))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 215 <= mouse_x <= 415 and 250 <= mouse_y <= 310 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Easy'

        if 215 <= mouse_x <= 415 and 330 <= mouse_y <= 390 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Intermediate'

        if 215 <= mouse_x <= 415 and 410 <= mouse_y <= 470 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Hard'

        if 815 <= mouse_x <= 1015 and 250 <= mouse_y <= 310 and click:
            if sfx_on:
                click_sfx.play()
            a2_status = 'Easy'

        if 815 <= mouse_x <= 1015 and 330 <= mouse_y <= 390 and click:
            if sfx_on:
                click_sfx.play()
            a2_status = 'Intermediate'

        if 815 <= mouse_x <= 1015 and 410 <= mouse_y <= 470 and click:
            if sfx_on:
                click_sfx.play()
            a2_status = 'Hard'

        if 470 <= mouse_x <= 770 and 500 <= mouse_y <= 580:
            pygame.draw.rect(screen, (255, 20, 20, 1), start_button, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), start_button, 5, 8)
            screen.blit(start_game, (535, 525))
            if click:
                if sfx_on:
                    click_sfx.play()
                if a1_status == 'Easy' and a2_status == 'Easy':
                    game_visualize.create_grid(game_code.RandomPlayer(), game_code.RandomPlayer())
                if a1_status == 'Easy' and a2_status == 'Intermediate':
                    game_visualize.create_grid(game_code.RandomPlayer(), game_code.IntermediatePlayer())
                if a1_status == 'Easy' and a2_status == 'Hard':
                    # TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    # TODO: Finally call one hard bot inside the body of create_grid after the random player
                    game_visualize.create_grid(game_code.RandomPlayer(), )
                if a1_status == 'Intermediate' and a2_status == 'Easy':
                    game_visualize.create_grid(game_code.IntermediatePlayer(), game_code.RandomPlayer())
                if a1_status == 'Intermediate' and a2_status == 'Intermediate':
                    game_visualize.create_grid(game_code.IntermediatePlayer(), game_code.IntermediatePlayer())
                if a1_status == 'Intermediate' and a2_status == 'Hard':
                    # TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    # TODO: Finally call one hard bot inside the body of create_grid after the intermediate player
                    game_visualize.create_grid(game_code.IntermediatePlayer(), hard_bot)
                if a1_status == 'Hard' and a2_status == 'Easy':
                    # TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    # TODO: Finally call one hard bot inside the body of create_grid before the random player
                    game_visualize.create_grid(, game_code.RandomPlayer())
                if a1_status == 'Hard' and a2_status == 'Intermediate':
                    # TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    # TODO: Finally call one hard bot inside the body of create_grid before the intermediate player
                    game_visualize.create_grid(, game_code.IntermediatePlayer())
                if a1_status == 'Hard' and a2_status == 'Hard':
                    # TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    # TODO: Finally call two hard bots inside the body of create_grid
                    game_visualize.create_grid(,)

        if a1_status == 'Easy':
            pygame.draw.rect(screen, (77, 175, 230, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (290, 265))
            screen.blit(intermediate, (225, 345))
            screen.blit(hard, (280, 425))

        if a1_status == 'Intermediate':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (290, 265))
            screen.blit(intermediate, (225, 345))
            screen.blit(hard, (280, 425))

        if a1_status == 'Hard':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (290, 265))
            screen.blit(intermediate, (225, 345))
            screen.blit(hard, (280, 425))

        if a2_status == 'Easy':
            pygame.draw.rect(screen, (77, 175, 230, 1), button_4, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_4, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_5, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_5, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_6, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_6, 5, 8)
            screen.blit(easy, (890, 265))
            screen.blit(intermediate, (825, 345))
            screen.blit(hard, (880, 425))

        if a2_status == 'Intermediate':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_4, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_4, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_5, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_5, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_6, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_6, 5, 8)
            screen.blit(easy, (890, 265))
            screen.blit(intermediate, (825, 345))
            screen.blit(hard, (880, 425))

        if a2_status == 'Hard':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_4, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_4, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_5, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_5, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_6, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_6, 5, 8)
            screen.blit(easy, (890, 265))
            screen.blit(intermediate, (825, 345))
            screen.blit(hard, (880, 425))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def play() -> None:
    """Display the player game-mode menu"""
    status = True
    click = False
    title_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 100)
    options_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 24)
    instruction_font = pygame.font.Font("assets/Misc/LEMonMILK-Regular.otf", 18)

    while status:
        global a1_status, a2_status
        screen.blit(background, (0, 0))
        title = title_font.render('PLAYER MODE', False, (255, 255, 255))
        screen.blit(title, (280, 5))

        escape = instruction_font.render('HIT ESC TO RETURN TO THE MAIN MENU', False, (255, 255, 255))
        screen.blit(escape, (25, 685))

        ai_1_text = options_font.render('Select AI Difficulty', False, (255, 255, 255))
        screen.blit(ai_1_text, (500, 200))

        button_1 = pygame.Rect((535.0, 250.0), (200.0, 60.0))
        button_2 = pygame.Rect((535.0, 330.0), (200.0, 60.0))
        button_3 = pygame.Rect((535.0, 410.0), (200.0, 60.0))
        start_button = pygame.Rect((485.0, 520.0), (300.0, 80.0))

        easy = options_font.render('Easy', False, (255, 255, 255))
        intermediate = options_font.render('Intermediate', False, (255, 255, 255))
        hard = options_font.render('Hard', False, (255, 255, 255))
        start_game = options_font.render('Start Game', False, (255, 255, 255))

        pygame.draw.rect(screen, (200, 0, 0, 1), start_button, 0, 8)
        pygame.draw.rect(screen, (0, 0, 0, 1), start_button, 5, 8)
        screen.blit(start_game, (555, 545))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 535 <= mouse_x <= 735 and 250 <= mouse_y <= 310 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Easy'

        if 535 <= mouse_x <= 735 and 330 <= mouse_y <= 390 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Intermediate'

        if 535 <= mouse_x <= 735 and 410 <= mouse_y <= 470 and click:
            if sfx_on:
                click_sfx.play()
            a1_status = 'Hard'

        if 485 <= mouse_x <= 785 and 520 <= mouse_y <= 600:
            pygame.draw.rect(screen, (255, 20, 20, 1), start_button, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), start_button, 5, 8)
            screen.blit(start_game, (555, 545))
            if click:
                if sfx_on:
                    click_sfx.play()
                if a1_status == 'Easy':
                    player.create_grid(game_code.RandomPlayer())
                if a1_status == 'Intermediate':
                    player.create_grid(game_code.IntermediatePlayer())
                if a1_status == 'Hard':
                    #TODO: initialize the hardbot tree here and other attributes that need to be initialized
                    #TODO: Finally call a hard bot inside the body of create_grid
                    player.create_grid()


        if a1_status == 'Easy':
            pygame.draw.rect(screen, (77, 175, 230, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (605, 265))
            screen.blit(intermediate, (550, 345))
            screen.blit(hard, (600, 425))

        if a1_status == 'Intermediate':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (605, 265))
            screen.blit(intermediate, (550, 345))
            screen.blit(hard, (600, 425))

        if a1_status == 'Hard':
            pygame.draw.rect(screen, (23, 113, 164, 1), button_1, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_1, 5, 8)
            pygame.draw.rect(screen, (23, 113, 164, 1), button_2, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_2, 5, 8)
            pygame.draw.rect(screen, (77, 175, 230, 1), button_3, 0, 8)
            pygame.draw.rect(screen, (0, 0, 0, 1), button_3, 5, 8)
            screen.blit(easy, (605, 265))
            screen.blit(intermediate, (550, 345))
            screen.blit(hard, (600, 425))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


main_menu()
