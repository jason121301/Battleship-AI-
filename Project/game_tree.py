"""The file that keeps track of the Game Trees that could be used.
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO."""

from __future__ import annotations
from typing import Optional

import game_code
import random
import copy


class WinningGameTree:
    """A gametree for battleship moves, intended to teach an AI an efficient way to play battleship
    ideally, being able to learn as much as at least intermediate bot or even more

    Instance Attributes
        - move: The current battleship move, based on tile shot
        - win_probability: the chance to win when making this move
        """
    move: str
    win_probability: float
    _subtrees: list[WinningGameTree]

    def __init__(self, move: str = 'first_move', win_probability: float = 0.0):
        self.move = move
        self.win_probability = win_probability
        self._subtrees = []

    def get_subtrees(self) -> list:
        """Get the subtrees of the Game Tree"""
        return self._subtrees

    def find_subtree_by_move(self, move: str) -> Optional[WinningGameTree]:
        """Return the subtree corresponding to the given move.

        Return None if no subtree corresponds to that move.
        """
        for subtree in self._subtrees:
            if subtree.move == move:
                return subtree

        return None

    def add_subtree(self, subtree: WinningGameTree) -> None:
        """Add a subtree to this game tree."""
        self._subtrees.append(subtree)
        self._update_win_probability()

    def insert_move_sequence(self, moves: list[str], win_probability: Optional[float]) -> None:
        """Inserts a sequence of moving that leads to either winning or losing in the Battleship
        Game"""
        self.insert_move_helper(moves, 0, win_probability)
        self._update_win_probability()
        return None

    def insert_move_helper(self, moves: list[str], index: int,
                           win_probability: Optional[float]) -> None:
        """Helper function for insert_move_sequence"""

        if index == len(moves):
            return None
        if self.find_subtree_by_move(moves[index]) is not None:
            return self.find_subtree_by_move(moves[index]). \
                insert_move_helper(moves, index + 1, win_probability)
        else:
            new_subtree = WinningGameTree(moves[index], win_probability)
            self.add_subtree(new_subtree)
            return new_subtree.insert_move_helper(moves, index + 1, win_probability)

    def _update_win_probability(self) -> None:
        """Update the win probability of this game tree. Updates it into the average
        of all the subtrees below it"""
        if self._subtrees == []:
            return None
        else:
            win_probability_so_far = []
            for subtree in self._subtrees:
                subtree._update_win_probability()
                win_probability_so_far.append(subtree.win_probability)
            self.win_probability = sum(win_probability_so_far) / len(win_probability_so_far)
            return None


class WinningGameTreePlayer(game_code.Player):
    """A player that chooses the best play from the game tree only. It chooses the play with
    the highest probability of winning"""
    game_tree: Optional[WinningGameTree]

    def __init__(self, game_tree: WinningGameTree) -> None:
        self.game_tree = game_tree

    def make_move(self, game: game_code.BattleshipGame, previous_move: str) -> str:
        """Make a move that chooses the move with the highest probability"""
        valid_moves = game.get_valid_moves()
        if self.game_tree is None:
            return random.choice(valid_moves)
        elif self.game_tree.get_subtrees() == []:
            self.game_tree = None
            return random.choice(valid_moves)
        elif self.game_tree.find_subtree_by_move(previous_move) is None:
            self.game_tree = None
            return random.choice(valid_moves)
        else:
            self.game_tree = self.game_tree.find_subtree_by_move(previous_move)
            move = self.game_tree.get_subtrees()[0].move
            highest = -1.0
            for subtree in self.game_tree.get_subtrees():
                if subtree.win_probability > highest:
                    highest = subtree.win_probability
                    move = subtree.move
            return move


class TileGameTree:
    """A game tree made to figure out the probability of a tile having a ship based on its
    previous moves instead of just the winning chance. Something specific like this
    will more likely learn effectively. In this Game Tree, whenever a shot that lands on a ship
    hits, it will then go to the subtree in order to find tiles near that which has the highest
    chance to also have a ship. The first _subtrees of the main root will contain all the tile
    along with its probabilities. Basically, the logic is that it will only go down the tree if it
    hits a ship. So that the GameTree is used to decide what the AI should do after hitting the ship
    while the original subtrees are used to see which tiles to specifically hit first
    to have the highest odds of hitting a ship.
    The goal of this TileGameTree
        - Teach the AI that middle tiles are most likely to have ships
        - Teach the AI that whenever a ship is hit, it needs to explore its surroundings
          to find other parts of the ship
    """
    move: str
    ship_probability: list[int, int]
    _subtrees: list[Optional[TileGameTree]]

    def __init__(self, move: str = 'first_move', ship_probability=None, subtrees=None):
        if subtrees is None:
            subtrees = []
        if ship_probability is None:
            ship_probability = [1, 1]
        self.move = move
        self.ship_probability = ship_probability
        if subtrees is None:
            self._subtrees = []
        else:
            self._subtrees = subtrees

    def add_subtree(self, subtree: TileGameTree) -> None:
        """Add a subtree to this TileGameTree."""
        self._subtrees.append(subtree)

    def get_subtrees(self) -> list:
        """Get the subtrees of the TileGameTree"""
        return self._subtrees

    def find_subtree_by_move(self, move: str) -> Optional[TileGameTree]:
        """Return the subtree corresponding to the given move.

        Return None if no subtree corresponds to that move.
        """
        for subtree in self._subtrees:
            if subtree.move == move:
                return subtree

        return None

    def ship_locator_fill(self, ship_locator: game_code.ShipLocatingPlayer) -> None:
        """Fills the Tile Game Tree with the probabilities obtained through the Ship Locator
        Player"""
        for position in ship_locator.tile_probability:
            new_subtree = TileGameTree(position, [ship_locator.tile_probability[position][0],
                                                  ship_locator.tile_probability[position][1]])
            self.add_subtree(new_subtree)
        return None

    def update_tile_probability(self, previous_move: list[str],
                                depth: int, final_hit: bool) -> None:
        """Update the tile probability of the tree, along with adding new subtrees
        if needed. Only recurse through a subtree and update the subtrees of the original 64
        if a hit is confirmed, otherwise, just update the tile probability of the initial 64
        moves"""
        if depth == 0:
            if self.find_subtree_by_move(previous_move[len(previous_move) - 1]) is None:
                if final_hit is True:
                    subtree = TileGameTree(previous_move[len(previous_move) - 1], [2, 2])
                    self.add_subtree(subtree)
                    return None
                else:
                    subtree = TileGameTree(previous_move[len(previous_move) - 1], [1, 2])
                    self.add_subtree(subtree)
                    return None
            else:
                updated_subtree = self.find_subtree_by_move(previous_move[len(previous_move) - 1])
                if final_hit is True:
                    updated_subtree.ship_probability[0] += 1
                    updated_subtree.ship_probability[1] += 1
                    return None
                else:
                    updated_subtree.ship_probability[1] += 1
                    return None
        else:
            if self.find_subtree_by_move(previous_move[len(previous_move) - 1 - depth]) is None:
                subtree = TileGameTree(previous_move[len(previous_move) - 1 - depth], [2, 2])
                self.add_subtree(subtree)
                subtree.update_tile_probability(previous_move, depth - 1, final_hit)
                return None
            else:
                subtree = self.find_subtree_by_move(previous_move[len(previous_move) - 1 - depth])
                subtree.ship_probability[0] += 1
                subtree.ship_probability[1] += 1
                subtree.update_tile_probability(previous_move, depth - 1, final_hit)
                return None

    def print_string(self) -> str:
        """Function used to print out the string representation of this Game Tree"""
        i = 0
        print_so_far = 'game_tree.TileGameTree(' + self.move + ',' + str(
            self.ship_probability) + ', ['
        if self._subtrees != []:
            for subtrees in self._subtrees:
                print_so_far += subtrees.print_string()
                i += 1
                if i != len(self._subtrees):
                    print_so_far += ','
        print_so_far += '])'
        return print_so_far


class TileTreePlayer(game_code.Player):
    """A player that chooses the best play from the game tree only. It chooses the play with
    the highest probability of finding a ship. The depth variable is the amount of time it has
    succesfully hit a ship, in which case the length of it represents how far into the subtree
    it should recurse to find the next succesful move."""
    game_tree: Optional[TileGameTree]
    depth: [str]
    ship_shot: int

    def __init__(self, game_tree: TileGameTree = TileGameTree()) -> None:
        self.game_tree = game_tree
        self.depth = []
        self.ship_shot = 0

    def update_depth(self, move: Optional[str], board: game_code.BattleshipGame) -> None:
        """Update the depth of this particular move combination. If the shot misses, then
        reset the depth counter into an empty list, otherwise, add the move into the
        depth list in order to recurse through the game tree properly. Additionally, update
        the game tree accordingly whenever it misses such that the previous move sequence
        is added into the game tree"""
        if self.ship_shot < board.ship_shot:
            self.ship_shot += 1
            self.depth.append(move)
            return None
        else:
            if move is not None:
                if self.depth == []:
                    self.game_tree.update_tile_probability([move], 0, False)
                else:
                    self.depth.append(move)
                    self.game_tree.update_tile_probability(self.depth, len(self.depth) - 1, False)
            self.depth = []
            return None

    def make_move(self, board: game_code.BattleshipGame, previous_move: Optional[str]):
        """Make move that is ideal considering the board state and the game tree
        along with the current depth"""
        self.update_depth(previous_move, board)
        possible_moves = board.get_valid_moves()
        if self.depth == []:
            highest_probability = 0
            best_move = random.choice(possible_moves)
            for subtree in self.game_tree.get_subtrees():
                if subtree.move in possible_moves and subtree.ship_probability[1] > 3:
                    if subtree.ship_probability[0] / \
                            subtree.ship_probability[1] > highest_probability:
                        highest_probability = \
                            subtree.ship_probability[0] / subtree.ship_probability[1]
                        best_move = subtree.move
            return best_move
        else:
            new_subtree = copy.deepcopy(self.game_tree)
            for move in self.depth:
                if new_subtree.find_subtree_by_move(move) is None:
                    return random.choice(possible_moves)
                else:
                    new_subtree = new_subtree.find_subtree_by_move(move)
                    highest_probability = 0
                    best_move = random.choice(possible_moves)
                    for subtree in new_subtree.get_subtrees():
                        if subtree.move in possible_moves and subtree.ship_probability[1] > 3:
                            if subtree.ship_probability[0] / \
                                    subtree.ship_probability[1] > highest_probability:
                                highest_probability = \
                                    subtree.ship_probability[0] / subtree.ship_probability[1]
                                best_move = subtree.move
                    return best_move
