"""This file contains the primary AI code for our project. This includes
the parent and subclasses for the battleship game and also both the 'easy' and 'intermediate'
player options.
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO
"""


from __future__ import annotations

import copy
import random
from typing import Optional

import plotly.graph_objects as go
from plotly.subplots import make_subplots


################################################################################
# Representing Battleship
################################################################################
_FILE_TO_INDEX = {'z': -1, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
_INDEX_TO_FILE = {i: f for f, i in _FILE_TO_INDEX.items()}
_RANK_TO_INDEX = {'0': -1, '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8}
_INDEX_TO_RANK = {i: r for r, i in _RANK_TO_INDEX.items()}

_MAX_MOVES = 200


class BattleshipGame:
    """A class representing a state of a game of Battleship.

    >>> game = BattleshipGame()
    >>> # Make a move. This method mutates the state of the game. Such that the tile is marked and is shot
    >>> game.make_move('A2')
    >>> # If you try to make an invalid move, a ValueError is raised.
    >>> game.make_move('A2')
    Traceback (most recent call last):
    ValueError: Move "a2" is not valid
    >>> # This move is okay.
    >>> game.make_move('B4')
    """
    # Private Instance Attributes:
    #   - _board: a two-dimensional representation of a Battleship board
    #   - _valid_moves: a list of the valid moves of the current player
    #   - _is_white_active: a boolean representing whether white is the current player
    #   - _move_count: the number of moves that have been made in the current game
    _board: list[list[Optional[Piece]]]
    _valid_moves: list[str]
    _move_count: int
    ship_shot: int

    def __init__(self, board: list[list[Optional[Piece]]] = None,
                 move_count: int = 0, ship_shot: int = 0) -> None:

        if board is not None:
            self._board = board
        else:
            self._board = [
                [None, None, None, None, None, None, None, None],
                [Piece('Ca'), Piece('Ca'), Piece('Ca'), Piece('Ca'),
                 Piece('Ca'), None, None, None],
                [None, None, None, None, None, None, None, None],
                [Piece('B'), Piece('B'), Piece('B'), Piece('B'),
                 None, None, None, None],
                [Piece('Cr'), Piece('Cr'), Piece('Cr'), None, None, None, None,
                 None],
                [None, None, None, Piece('S'), Piece('S'), Piece('S'), None,
                 None],
                [None, None, None, Piece('D'), Piece('D'), None, None, None],
                [None, None, None, None, None, None, None, None]
            ]
        self._move_count = move_count
        self._valid_moves = []
        self.ship_shot = ship_shot

        self._recalculate_valid_moves()

    def get_board(self) -> list[list[Optional[Piece]]]:
        """Return the board of the Battleship Game"""
        return self._board

    def get_num_moves(self) -> int:
        """Return the number of moves played"""
        return self._move_count

    def get_valid_moves(self) -> list[str]:
        """Return a list of the valid moves for the active player."""
        return self._valid_moves

    def make_move(self, move: str) -> None:
        """Make the given shot. This instance of Battleship will be mutated, and will
        afterwards represent the game state after move is made.

        If move is not a currently valid move, raise a ValueError.
        """
        if move not in self._valid_moves:
            raise ValueError(f'Move "{move}" is not valid')
        if self._board_after_move(move)[1] is True:
            self.ship_shot += 1
        self._board = self._board_after_move(move)[0]

        self._move_count += 1

        self._recalculate_valid_moves()

    def copy_and_make_move(self, move: str) -> BattleshipGame:
        """Make the given move in a copy of this BattleshipGame, and return that copy.
        If a ship is shot, kep track of that occurence in the ship_shot variable.

        If move is not a currently valid move, raise a ValueError.
        """
        if self._board_after_move(move)[1] is True:
            return BattleshipGame(board=self._board_after_move(move)[0],
                                  move_count=self._move_count + 1, ship_shot=self.ship_shot + 1)
        else:
            return BattleshipGame(board=self._board_after_move(move)[0],
                                  move_count=self._move_count + 1, ship_shot=self.ship_shot)

    def get_winner(self) -> Optional[str]:
        """Return draw if moves are above max_move or a loss if all the ships are shot.
        All the ships combined total into 17 tiles, therefore, when 17 ships are shot
        the player has lost

        Return None if the game is not over.
        """
        if self.ship_shot == 17:
            return 'Lost'
        elif len(self._valid_moves) == 0:
            return 'Draw'
        else:
            return None

    def _calculate_moves_for_board(self, board: list[list[Optional[Piece]]]) -> list[str]:
        """Return all possible moves on a given board with a given active player."""
        moves = []

        for pos in [(y, x) for y in range(0, 8) for x in range(0, 8)]:
            piece = board[pos[0]][pos[1]]
            if piece is None:
                moves.append(_index_to_algebraic(pos))
            else:
                kind = piece.kind
                if kind == 'M' or kind == 'H':
                    continue
                else:
                    moves.append(_index_to_algebraic(pos))
        return moves

    def _board_after_move(self, move: str) -> tuple[list[list[Optional[Piece]]], bool]:
        """Return a copy of self._board representing the state of the board after making a shot."""
        board_copy = copy.deepcopy(self._board)

        shot_location = _algebraic_to_index(move)
        if board_copy[shot_location[0]][shot_location[1]] is None:
            board_copy[shot_location[0]][shot_location[1]] = Piece('M')
            ship_shot = False
        else:
            board_copy[shot_location[0]][shot_location[1]] = Piece('H')
            ship_shot = True

        return (board_copy, ship_shot)

    def _recalculate_valid_moves(self) -> None:
        """Update the valid moves for this game board. In which valid moves are
        shooting empty tiles which has not been shot yet"""

        self._valid_moves = self._calculate_moves_for_board(self._board)


def _algebraic_to_index(move: str) -> tuple[int, int]:
    """Convert coordinates in algebraic format ex. 'a2' to array indices (y, x)."""
    return (_RANK_TO_INDEX[move[1]], _FILE_TO_INDEX[move[0]])


def _index_to_algebraic(pos: tuple[int, int]) -> str:
    """Convert coordinates in array indices (y, x) to algebraic format."""
    return _INDEX_TO_FILE[pos[1]] + _INDEX_TO_RANK[pos[0]]


class RandomizedBattleshipGame(BattleshipGame):
    """Instead of a battleship games with ship at the same positions, the
    ships will be randomized for this battleship game"""

    def __init__(self, board: list[list[Optional[Piece]]] = None, move_count: int = 0,
                 ship_shot: int = 0) -> None:

        super().__init__(board, move_count, ship_shot)
        if board is not None:
            self._board = board
        else:
            self._board = [
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None]
            ]
            carrier_axis = random.randint(0, 1)
            space_taken = []
            if carrier_axis == 1:
                carrier_pool = [(y, x) for y in range(0, 3) for x in range(0, 8)]
                carrier_start = random.choice(carrier_pool)
                carrier = [(carrier_start[0] + i, carrier_start[1]) for i in range(0, 5)]
            else:
                carrier_pool = [(y, x) for y in range(0, 8) for x in range(0, 3)]
                carrier_start = random.choice(carrier_pool)
                carrier = [(carrier_start[0], carrier_start[1] + i) for i in range(0, 5)]
            space_taken.extend(carrier)
            battleship_axis = random.randint(0, 1)
            if battleship_axis == 1:
                battleship_pool = [(y, x) for y in range(0, 4) for x in range(0, 8) if
                                   (y, x) not in carrier and (y + 3, x) not in carrier
                                   and (y + 1, x) not in carrier and (y + 2, x) not in carrier]
                battleship_start = random.choice(battleship_pool)
                battleship = [(battleship_start[0] + i, battleship_start[1]) for i in range(0, 4)]
            else:
                battleship_pool = [(y, x) for y in range(0, 8) for x in range(0, 4)
                                   if (y, x) not in carrier and (y, x + 3) not in carrier
                                   and (y, x + 1) not in carrier and (y, x + 2) not in carrier]
                battleship_start = random.choice(battleship_pool)
                battleship = [(battleship_start[0], battleship_start[1] + i) for i in range(0, 4)]
            space_taken.extend(battleship)
            cruiser_axis = random.randint(0, 1)
            if cruiser_axis == 1:
                cruiser_pool = [(y, x) for y in range(0, 5) for x in range(0, 8) if
                                (y, x) not in space_taken and (y + 2, x) not in space_taken
                                and (y + 1, x) not in space_taken]
                cruiser_start = random.choice(cruiser_pool)
                cruiser = [(cruiser_start[0] + i, cruiser_start[1]) for i in range(0, 3)]
            else:
                cruiser_pool = [(y, x) for y in range(0, 8) for x in range(0, 5)
                                if (y, x) not in space_taken and (y, x + 2) not in space_taken
                                and (y, x + 1) not in space_taken]
                cruiser_start = random.choice(cruiser_pool)
                cruiser = [(cruiser_start[0], cruiser_start[1] + i) for i in range(0, 3)]
            space_taken.extend(cruiser)
            sub_axis = random.randint(0, 1)
            if sub_axis == 1:
                sub_pool = [(y, x) for y in range(0, 5) for x in range(0, 8) if
                            (y, x) not in space_taken and (y + 2, x) not in space_taken
                            and (y + 1, x) not in space_taken]
                sub_start = random.choice(sub_pool)
                sub = [(sub_start[0] + i, sub_start[1]) for i in range(0, 3)]
            else:
                sub_pool = [(y, x) for y in range(0, 8) for x in range(0, 5)
                            if (y, x) not in space_taken and (y, x + 2) not in space_taken
                            and (y, x + 1) not in space_taken]
                sub_start = random.choice(sub_pool)
                sub = [(sub_start[0], sub_start[1] + i) for i in range(0, 3)]
            space_taken.extend(sub)
            des_axis = random.randint(0, 1)
            if des_axis == 1:
                des_pool = [(y, x) for y in range(0, 6) for x in range(0, 8) if
                            ((y, x) not in space_taken and (y + 1, x) not in space_taken)]
                des_start = random.choice(des_pool)
                destroyer = [(des_start[0] + i, des_start[1]) for i in range(0, 2)]
            else:
                des_pool = [(y, x) for y in range(0, 8) for x in range(0, 6)
                            if (y, x) not in space_taken and (y, x + 1) not in space_taken]
                des_start = random.choice(des_pool)
                destroyer = [(des_start[0], des_start[1] + i) for i in range(0, 2)]
            for coord in carrier:
                self._board[coord[0]][coord[1]] = Piece('Ca')
            for coord in battleship:
                self._board[coord[0]][coord[1]] = Piece('B')
            for coord in cruiser:
                self._board[coord[0]][coord[1]] = Piece('Cr')
            for coord in sub:
                self._board[coord[0]][coord[1]] = Piece('S')
            for coord in destroyer:
                self._board[coord[0]][coord[1]] = Piece('D')

        self._move_count = move_count
        self._valid_moves = []
        self.ship_shot = ship_shot

        self._recalculate_valid_moves()


class Piece:
    """Represents a single piece in Battleship.

    Instance Attributes:
        - kind: the type of piece
    """
    kind: str  # One of  {'Ca','B','Cr','S','D', 'H', 'M'}

    def __init__(self, kind: str) -> None:
        """Initialize a new piece."""
        self.kind = kind


################################################################################
# Battleship Player Classes
################################################################################
class Player:
    """An abstract class representing a Battleship AI.

    This class can be subclassed to implement different strategies for playing chess.
    """
    ship_shot: int

    def __init__(self) -> None:
        self.ship_shot = 0

    def make_move(self, game: BattleshipGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.

        previous_move is the opponent player's most recent move, or None if no moves
        have been made.

        Preconditions:
            - There is at least one valid move for the given game
        """
        raise NotImplementedError


class RandomPlayer(Player):
    """A Battleship AI whose strategy is always picking a random move."""

    def make_move(self, game: BattleshipGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.

        previous_move is the opponent player's most recent move, or None if no moves
        have been made.

        Preconditions:
            - There is at least one valid move for the given game
        """
        possible_moves = game.get_valid_moves()
        return random.choice(possible_moves)


class IntermediatePlayer(Player):
    """A Battleship AI who tries to shoot near the point of impact after finding the ship"""

    def make_move(self, game: BattleshipGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.
        previous_move is the current player's most recent move, or None if no moves had been made
        Preconditions:
            - There is at least one valid move for the given game
        """
        possible_moves = game.get_valid_moves()
        if previous_move is None:
            return random.choice(possible_moves)
        prev = _algebraic_to_index(previous_move)
        if game.ship_shot > self.ship_shot:
            self.ship_shot += 1
            horizontal = [_index_to_algebraic((prev[0] - 1 + i, prev[1])) for i in range(0, 3)
                          if _index_to_algebraic((prev[0] - 1 + i, prev[1])) in possible_moves]
            vertical_tiles = [_index_to_algebraic((prev[0], prev[1] - 1 + i)) for i in range(0, 3)
                              if _index_to_algebraic((prev[0], prev[1] - 1 + i)) in possible_moves]
            options = horizontal + vertical_tiles
            if options != []:
                return random.choice(options)
        return random.choice(possible_moves)


class ShipLocatingPlayer(Player):
    """A battleship AI specifically focused on finding tiles which has the highest probability
    of having a ship in it. Whenever a ship is shot on a certain tile, keep track of it by
    adding a counter into tile_probability. Shot the tile that has the highest probabiltiy
    of hitting"""
    tile_probability: dict

    def __init__(self, tile_probability: Optional[dict] = None) -> None:
        """Initializes this player, creating a tile_probability dictionary containing all the
        tile"""
        super().__init__()
        if tile_probability is None:
            self.tile_probability = {x: [1, 1] for x in
                                     ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2',
                                      'C2',
                                      'D2', 'E2', 'F2', 'G2', 'H2', 'A3', 'B3', 'C3', 'D3', 'E3',
                                      'F3',
                                      'G3', 'H3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
                                      'A5',
                                      'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'A6', 'B6', 'C6',
                                      'D6',
                                      'E6', 'F6', 'G6', 'H6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7',
                                      'G7',
                                      'H7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']}
        else:
            self.tile_probability = tile_probability

    def make_move(self, game: BattleshipGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.
        previous_move is the player's most recent move, or None if no moves
        have been made.
        Preconditions:
            - There is at least one valid move for the given game
        """

        highest_value = -1
        possible_moves = game.get_valid_moves()
        highest_move = random.choice(possible_moves)
        if previous_move is None:
            for moves in self.tile_probability:
                if moves in possible_moves:
                    if self.tile_probability[moves][0] / self.tile_probability[moves][1] \
                            > highest_value:
                        highest_move = moves
                        highest_value = \
                            self.tile_probability[moves][0] / self.tile_probability[moves][1]
            return highest_move

        self.tile_probability[previous_move][1] += 1

        if self.ship_shot < game.ship_shot:
            self.tile_probability[previous_move][0] += 1
            self.ship_shot += 1
        for moves in self.tile_probability:
            if moves in possible_moves:
                if self.tile_probability[moves][0] / self.tile_probability[moves][1] \
                        > highest_value:
                    highest_move = moves
                    highest_value = \
                        self.tile_probability[moves][0] / self.tile_probability[moves][1]
        return highest_move


################################################################################
# Functions for running games
################################################################################


def run_games(n: int, player_1: Player, player_2: Player,
              show_stats: bool = False) -> None:
    """Run n games using the given Players.

    Optional arguments:
        - show_stats: whether to use Plotly to display statistics for the game runs

    Preconditions:
        - n >= 1
        - fps >= 1
    """

    stats = {'Player1': 0, 'Player2': 0}
    results = []
    for i in range(0, n):
        player_1_copy = copy.deepcopy(player_1)
        player_2_copy = copy.deepcopy(player_2)

        winner, _, _ = run_game(player_1_copy, player_2_copy)
        stats[winner] += 1
        results.append(winner)

        print(f'Game {i} winner: {winner}')

    for outcome in stats:
        print(f'{outcome}: {stats[outcome]}/{n} ({100.0 * stats[outcome] / n:.2f}%)')

    if show_stats:
        plot_game_statistics(results)


def run_game(player1: Player, player2: Player) -> tuple[str, list[str], list[str]]:
    """Run a Battleship game between the two given players.

    Return the winner and list of moves made in the game.
    """
    p1_board = RandomizedBattleshipGame()
    p2_board = RandomizedBattleshipGame()
    player1.ship_shot = 0
    player2.ship_shot = 0
    p1_move_sequence = []
    p2_move_sequence = []
    p1_previous_move = None
    p2_previous_move = None
    while p1_board.get_winner() is None and p2_board.get_winner() is None:
        # player1's shot on player2's board
        p1_previous_move = player1.make_move(p2_board, p1_previous_move)
        p2_board.make_move(p1_previous_move)
        p1_move_sequence.append(p1_previous_move)
        # player2's shot on player1's board
        p2_previous_move = player2.make_move(p1_board, p2_previous_move)
        p1_board.make_move(p2_previous_move)
        p2_move_sequence.append(p2_previous_move)

    if p2_board.get_winner() == 'Lost':
        winner = 'Player1'
    else:
        winner = 'Player2'

    return winner, p2_move_sequence, p1_move_sequence


def plot_game_statistics(results: list[str]) -> None:
    """Plot the outcomes and win probabilities for a given list of Battleship game results.

    Preconditions:
        - all(r in {'Player1', 'Player2'} for r in results)
    """
    outcomes = [1 if result == 'Player1' else 0 for result in results]
    outcomes_p2 = [1 if result == 'Player2' else 0 for result in results]

    cumulative_win_probability = [sum(outcomes[0:i]) / i for i in range(1, len(outcomes) + 1)]
    rolling_win_probability = \
        [sum(outcomes[max(i - 50, 0):i]) / min(50, i) for i in range(1, len(outcomes) + 1)]
    cumulative_p2_win = [sum(outcomes_p2[0:i]) / i for i in range(1, len(outcomes_p2) + 1)]
    rolling_p2_win = \
        [sum(outcomes_p2[max(i - 50, 0):i]) / min(50, i) for i in range(1, len(outcomes_p2) + 1)]

    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(y=outcomes, mode='markers',
                             name='Outcome (1 = Player 1 Win, 0 = Player 2 Win)'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(y=cumulative_win_probability, mode='lines',
                             name='Player 1 percentage (cumulative)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=rolling_win_probability, mode='lines',
                             name='Player 1 percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=cumulative_p2_win, mode='lines',
                             name='Player 2 percentage (cumulative)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=rolling_p2_win, mode='lines',
                             name='Player 2 percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.update_yaxes(range=[0.0, 1.0], row=2, col=1)

    fig.update_layout(title='Battleship Game Results', xaxis_title='Game')
    fig.show()
