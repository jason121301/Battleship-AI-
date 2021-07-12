"""This file contains all the learning algorithm in which a GameTree is used to develop
a smart player or 'hard bot'
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO"""

import game_code
import game_tree


def simple_learning(games: int, type_of_player: game_code.Player,
                    type_of_enemy: game_code.Player) -> game_code.Player:
    """Teaches a Game Tree Player and returns that said player. Trains it for the specific
    amount of game mentioned. Teaches it to make moves based on a specific bot too versus
    a specific enemy, (for example, when IntermediatePlayer is inputted, it will play
    like IntermediatePlayer and build a game tree based on that playstyle"""
    learning_tree = game_tree.WinningGameTree()
    for _ in range(0, games):
        results = game_code.run_game(type_of_player, type_of_enemy)
        if results[0] == "p1":
            learning_tree.insert_move_sequence(results[1], 1)
        else:
            learning_tree.insert_move_sequence(results[1], 0)
    trained_player = game_tree.WinningGameTreePlayer(learning_tree)
    return trained_player


def train_tile_probability(player: game_code.ShipLocatingPlayer, games: int) -> \
        game_code.ShipLocatingPlayer:
    """Teaches a Ship Locating Player the spots which most likely has ships by running through
    a certain amount of games and keeping track of where the ships are. Return that player in
    the end"""
    for i in range(0, games):
        random_board = game_code.RandomizedBattleshipGame()
        previous_move = None
        player.ship_shot = 0
        while len(random_board.get_valid_moves()) != 0:
            previous_move = player.make_move(random_board, previous_move)
            random_board.make_move(previous_move)
        print(i)
    player.ship_shot = 0
    return player


def train_after_hit_targeting(player: game_code.ShipLocatingPlayer, games: int) -> \
        game_tree.TileTreePlayer:
    """Teaches a Ship Locating Player how to locate other parts of ships after
    hitting a part of it. Returns as a Tile Tree Player"""
    tile_player = game_tree.TileTreePlayer()
    tile_player.game_tree.ship_locator_fill(player)
    for i in range(0, games):
        random_board = game_code.RandomizedBattleshipGame()
        intermediate = game_code.IntermediatePlayer()
        player.ship_shot = 0
        intermediate.ship_shot = 0
        ship_shot = 0
        previous_move = None
        move_sequence = []
        while len(random_board.get_valid_moves()) != 0:
            if random_board.ship_shot == ship_shot:
                previous_move = intermediate.make_move(random_board, previous_move)
                if move_sequence != []:
                    tile_player.game_tree.update_tile_probability(move_sequence,
                                                                  len(move_sequence) - 1, False)
                move_sequence = list()
                random_board.make_move(previous_move)
                move_sequence.append(previous_move)
            else:  # ship_shot < random_board.ship_shot
                previous_move = intermediate.make_move(random_board, previous_move)
                random_board.make_move(previous_move)
                move_sequence.append(previous_move)
                ship_shot += 1
        if len(move_sequence) > 1:
            tile_player.game_tree.update_tile_probability(move_sequence,
                                                          len(move_sequence) - 1, True)
        print(i)

    tile_player.ship_shot = 0
    return tile_player


def train_tile_player(player1: game_tree.TileTreePlayer,
                      player2: game_code.Player, games: int) -> game_tree.TileTreePlayer:
    """Trains a tile Tree player by running it on a randomized game against another player"""
    for i in range(0, games):
        player1.ship_shot = 0
        player2.ship_shot = 0
        game_code.run_game(player1, player2)
        print(i)
    player1.ship_shot = 0
    return player1


def generate_hard_bot(games1: int, games2: int) -> game_tree.TileTreePlayer:
    """Generate hard bot with games1 being the amount of games for the locator training,
    while games 2 the amount of games for the tile training"""
    locator = game_code.ShipLocatingPlayer()
    trained_locator = train_tile_probability(locator, games1)
    return train_after_hit_targeting(trained_locator, games2)
