"""This is the main python file, run this function and input your desired use of our program to have some fun or
investigate the win-rate of our AI bots! We hope you enjoy the game we put together to work with our AI! :)
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO"""

import game_code
import algorithm_learning
import game_tree
import hard_bot

AI1 = None
AI2 = None


def project_runner() -> None:
    """Run the project code based on user input"""
    print('Welcome to the launcher of our CSC111 Final Project!')
    print("Would you like to play a game of battleship or perform a win rate simulation for one of our bots?")
    greeting = None
    while greeting != 'Game' and greeting != 'Simulation':
        greeting = input("Please enter 'Game' or 'Simulation'")
        if greeting == 'Game':
            import GameWindow
            GameWindow.main_menu()
        elif greeting == 'Simulation':
            simulation_runner()
        else:
            print('Invalid Input, try again')


def hard_bot_picker() -> game_tree.TileTreePlayer():
    """Return a hard bot based on the gametree preference of the user."""
    global AI1, AI2
    print('Would you like to generate a new tree or the provided hard_bot tree?')
    print('NOTE: GENERATING A NEW BOT HAS VARYING RUNTIME BASED ON YOUR SYSTEM AND DESIRED GAME RUNS')
    tree_type = input("Type 'Default' for the pre-made tree, 'New' if you want to create a new one")
    if tree_type == 'Default':
        return hard_bot.return_hard_bot()
    elif tree_type == 'New':
        print('How experienced should your bot be? (i.e. how many games should it play?)')
        num_games = int(input('Enter the number of games'))
        if num_games > 0:
            return algorithm_learning.generate_hard_bot(num_games, num_games)
        else:
            return None


def simulation_runner() -> None:
    """Run a simulation based on the users selection"""
    global AI1, AI2
    print("Select Difficulty for AI 1")
    print('-Easy')
    print('-Intermediate')
    print('-Hard')
    while AI1 is None:
        num_1_selection = input("Please input your preference for first AI Player by typing its difficulty")
        if num_1_selection == 'Easy':
            AI1 = game_code.RandomPlayer()
        elif num_1_selection == 'Intermediate':
            AI1 = game_code.IntermediatePlayer()
        elif num_1_selection == 'Hard':
            AI1 = hard_bot_picker()
        else:
            print('Invalid Input, try again')

    print("Select Difficulty for AI 1")
    print('-Easy')
    print('-Intermediate')
    print('-Hard')
    while AI2 is None:
        num_2_selection = input("Please input your preference for second AI Player by typing its difficulty")
        if num_2_selection == 'Easy':
            AI2 = game_code.RandomPlayer()
        elif num_2_selection == 'Intermediate':
            AI2 = game_code.IntermediatePlayer()
        elif num_2_selection == 'Hard':
            AI2 = hard_bot_picker()
        else:
            print('Invalid Input, try again')
    num_games = -1
    while num_games <= 0:
        num_games = int(input('How many games do you want to play?'))
    game_code.run_games(num_games, AI1, AI2, True)


project_runner()
