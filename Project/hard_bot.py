"""The hard bot initializer. This hard bot has been train with 1000 games and is printed out
such that the game would not have to rerun the bot every single time it is loaded in.
COPYRIGHT 2021: JASON SASTRA AND MARTON KOVACS UNIVERSITY OF TORONTO."""

import game_tree


def return_hard_bot() -> game_tree.TileTreePlayer():
    """Return the pre-generated hard_bot that is ready to play"""
    player = hard_bot
    player.ship_shot = 0
    return player


first_move = 'first_move'
A1, A2, A3, A4, A5, A6, A7, A8 = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'
B1, B2, B3, B4, B5, B6, B7, B8 = 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'
C1, C2, C3, C4, C5, C6, C7, C8 = 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'
D1, D2, D3, D4, D5, D6, D7, D8 = 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'
E1, E2, E3, E4, E5, E6, E7, E8 = 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'
F1, F2, F3, F4, F5, F6, F7, F8 = 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'
G1, G2, G3, G4, G5, G6, G7, G8 = 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8'
H1, H2, H3, H4, H5, H6, H7, H8 = 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'

hard_bot = game_tree.TileTreePlayer(game_tree.TileGameTree(first_move, [1, 1], [
    game_tree.TileGameTree(A1, [98, 785], [game_tree.TileGameTree(A2, [20, 32], [
        game_tree.TileGameTree(B8, [1, 2], []),
        game_tree.TileGameTree(B2, [2, 8], [game_tree.TileGameTree(B1, [1, 2], [])]),
        game_tree.TileGameTree(A3, [7, 10], [game_tree.TileGameTree(E3, [1, 2], []),
                                             game_tree.TileGameTree(B3, [2, 3], [
                                                 game_tree.TileGameTree(B4, [1, 2], [])]),
                                             game_tree.TileGameTree(C4, [1, 2], []),
                                             game_tree.TileGameTree(A4, [2, 3], [
                                                 game_tree.TileGameTree(B4, [1, 2], [])])]),
        game_tree.TileGameTree(A8, [1, 2], []), game_tree.TileGameTree(G7, [1, 2], [])]),
                                           game_tree.TileGameTree(H5, [3, 3], [
                                               game_tree.TileGameTree(H8, [1, 2], []),
                                               game_tree.TileGameTree(H6, [2, 2], [
                                                   game_tree.TileGameTree(C8, [1, 2], [])])]),
                                           game_tree.TileGameTree(B1, [15, 32], [
                                               game_tree.TileGameTree(E2, [2, 2], [
                                                   game_tree.TileGameTree(E1, [2, 2], [
                                                       game_tree.TileGameTree(F1, [1, 2], [])])]),
                                               game_tree.TileGameTree(C1, [3, 4], [
                                                   game_tree.TileGameTree(G8, [1, 2], []),
                                                   game_tree.TileGameTree(D1, [2, 2], [
                                                       game_tree.TileGameTree(D2, [1, 2], [])])]),
                                               game_tree.TileGameTree(E7, [1, 2], []),
                                               game_tree.TileGameTree(B2, [2, 9], [
                                                   game_tree.TileGameTree(A2, [1, 2], [])]),
                                               game_tree.TileGameTree(F7, [1, 2], [])]),
                                           game_tree.TileGameTree(B6, [3, 3], [
                                               game_tree.TileGameTree(B7, [2, 2], [
                                                   game_tree.TileGameTree(F4, [1, 2], [])]),
                                               game_tree.TileGameTree(A6, [1, 2], [])]),
                                           game_tree.TileGameTree(C4, [1, 3], []),
                                           game_tree.TileGameTree(H1, [1, 2], []),
                                           game_tree.TileGameTree(A3, [2, 2], [
                                               game_tree.TileGameTree(A4, [2, 2], [
                                                   game_tree.TileGameTree(D2, [1, 2], [])])]),
                                           game_tree.TileGameTree(A8, [1, 2], []),
                                           game_tree.TileGameTree(G6, [2, 2], []),
                                           game_tree.TileGameTree(G7, [1, 2], []),
                                           game_tree.TileGameTree(F7, [1, 3], []),
                                           game_tree.TileGameTree(C7, [1, 2], []),
                                           game_tree.TileGameTree(F8, [1, 2], []),
                                           game_tree.TileGameTree(B7, [1, 2], []),
                                           game_tree.TileGameTree(D2, [1, 2], []),
                                           game_tree.TileGameTree(H2, [1, 2], []),
                                           game_tree.TileGameTree(C1, [1, 2], [])]),
    game_tree.TileGameTree(B1, [138, 761], [game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(B2, [13, 30], [
                                                game_tree.TileGameTree(A2, [1, 7], []),
                                                game_tree.TileGameTree(B3, [3, 4], [
                                                    game_tree.TileGameTree(B4, [2, 2], [
                                                        game_tree.TileGameTree(A4, [1, 2], [])]),
                                                    game_tree.TileGameTree(A3, [2, 2], [
                                                        game_tree.TileGameTree(A4, [2, 2], [
                                                            game_tree.TileGameTree(A5, [2, 2], [
                                                                game_tree.TileGameTree(A6, [2, 2], [
                                                                    game_tree.TileGameTree(A7,
                                                                                           [1, 2],
                                                                                           [])])])])])]),
                                                game_tree.TileGameTree(C2, [2, 4], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(E2, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(C1, [21, 37], [
                                                game_tree.TileGameTree(D1, [6, 7], [
                                                    game_tree.TileGameTree(E1, [4, 5], [
                                                        game_tree.TileGameTree(F1, [1, 3], []),
                                                        game_tree.TileGameTree(E8, [1, 2], [])]),
                                                    game_tree.TileGameTree(D2, [1, 2], [])]),
                                                game_tree.TileGameTree(D8, [1, 2], []),
                                                game_tree.TileGameTree(C2, [6, 10], [
                                                    game_tree.TileGameTree(C3, [2, 3], [
                                                        game_tree.TileGameTree(C4, [1, 2], [])]),
                                                    game_tree.TileGameTree(B2, [2, 2], [
                                                        game_tree.TileGameTree(A2, [2, 2], [
                                                            game_tree.TileGameTree(A1, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D2, [1, 3], [])]),
                                                game_tree.TileGameTree(E8, [1, 2], []),
                                                game_tree.TileGameTree(E6, [1, 2], []),
                                                game_tree.TileGameTree(F3, [1, 2], []),
                                                game_tree.TileGameTree(E5, [1, 2], [])]),
                                            game_tree.TileGameTree(C7, [2, 2], [
                                                game_tree.TileGameTree(C6, [2, 2], [
                                                    game_tree.TileGameTree(G4, [2, 2], [
                                                        game_tree.TileGameTree(D5, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(A1, [22, 42], [
                                                game_tree.TileGameTree(A2, [5, 17], [
                                                    game_tree.TileGameTree(F8, [2, 2], [
                                                        game_tree.TileGameTree(G8, [1, 2], [])]),
                                                    game_tree.TileGameTree(B2, [2, 4], [
                                                        game_tree.TileGameTree(B3, [1, 2], [])])]),
                                                game_tree.TileGameTree(D8, [1, 2], []),
                                                game_tree.TileGameTree(G1, [1, 2], []),
                                                game_tree.TileGameTree(E4, [2, 2], [
                                                    game_tree.TileGameTree(E3, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(D4, [2, 2], [
                                                                game_tree.TileGameTree(D5, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(A7, [1, 2], [])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(E5, [2, 3], []),
                                            game_tree.TileGameTree(F8, [2, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(H8, [2, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(D5, [2, 2], [
                                                game_tree.TileGameTree(D4, [2, 2], [
                                                    game_tree.TileGameTree(E4, [1, 2], [])])])]),
    game_tree.TileGameTree(C1, [173, 750], [game_tree.TileGameTree(D1, [42, 49], [
        game_tree.TileGameTree(E1, [21, 23], [game_tree.TileGameTree(E2, [1, 10], []),
                                              game_tree.TileGameTree(F1, [7, 11], [
                                                  game_tree.TileGameTree(G1, [5, 5], [
                                                      game_tree.TileGameTree(H1, [1, 3], []),
                                                      game_tree.TileGameTree(F3, [1, 2], []),
                                                      game_tree.TileGameTree(G2, [1, 2], [])]),
                                                  game_tree.TileGameTree(F2, [1, 2], []),
                                                  game_tree.TileGameTree(E7, [1, 2], [])]),
                                              game_tree.TileGameTree(G7, [2, 2], [
                                                  game_tree.TileGameTree(D5, [1, 2], [])])]),
        game_tree.TileGameTree(D2, [6, 16], [game_tree.TileGameTree(D3, [1, 4], []),
                                             game_tree.TileGameTree(E2, [2, 2], [
                                                 game_tree.TileGameTree(H7, [1, 2], [])])]),
        game_tree.TileGameTree(A1, [1, 2], []), game_tree.TileGameTree(H1, [1, 2], []),
        game_tree.TileGameTree(H3, [2, 2], [
            game_tree.TileGameTree(H2, [2, 2], [game_tree.TileGameTree(H1, [1, 2], [])])]),
        game_tree.TileGameTree(B8, [1, 2], [])]), game_tree.TileGameTree(C2, [16, 45], [
        game_tree.TileGameTree(C3, [4, 5], [game_tree.TileGameTree(B3, [2, 3], [
            game_tree.TileGameTree(B2, [2, 2], [game_tree.TileGameTree(B1, [2, 2], [
                game_tree.TileGameTree(A1, [2, 2], [game_tree.TileGameTree(A2, [1, 2], [])])])])]),
                                            game_tree.TileGameTree(C4, [2, 2], [
                                                game_tree.TileGameTree(E4, [1, 2], [])])]),
        game_tree.TileGameTree(B2, [1, 5], []), game_tree.TileGameTree(D2, [4, 6], [
            game_tree.TileGameTree(E2, [2, 2], [game_tree.TileGameTree(E1, [1, 2], [])]),
            game_tree.TileGameTree(D3, [1, 3], [])]), game_tree.TileGameTree(H6, [1, 2], []),
        game_tree.TileGameTree(B5, [1, 2], [])]), game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(B1, [20, 34], [
                                                game_tree.TileGameTree(A1, [8, 13], [
                                                    game_tree.TileGameTree(G5, [1, 2], []),
                                                    game_tree.TileGameTree(A2, [2, 5], [
                                                        game_tree.TileGameTree(B2, [1, 2], [])]),
                                                    game_tree.TileGameTree(G8, [2, 2], [
                                                        game_tree.TileGameTree(F8, [2, 2], [
                                                            game_tree.TileGameTree(E8, [2, 2], [
                                                                game_tree.TileGameTree(E7, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(B8, [1, 2], [])]),
                                                game_tree.TileGameTree(B2, [3, 6], [
                                                    game_tree.TileGameTree(A2, [1, 2], []),
                                                    game_tree.TileGameTree(B3, [1, 2], [])]),
                                                game_tree.TileGameTree(F5, [1, 2], []),
                                                game_tree.TileGameTree(H4, [1, 2], [])]),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(A7, [3, 4], [
                                                game_tree.TileGameTree(A6, [1, 2], [])]),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 3], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 3], []),
                                            game_tree.TileGameTree(E2, [1, 2], []),
                                            game_tree.TileGameTree(H7, [2, 4], [
                                                game_tree.TileGameTree(E8, [2, 2], [
                                                    game_tree.TileGameTree(F6, [1, 2], [])])]),
                                            game_tree.TileGameTree(C8, [2, 2], []),
                                            game_tree.TileGameTree(B6, [2, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 2], [])]),
    game_tree.TileGameTree(D1, [179, 731], [game_tree.TileGameTree(E1, [25, 37], [
        game_tree.TileGameTree(E2, [3, 11], [
            game_tree.TileGameTree(D2, [2, 3], [game_tree.TileGameTree(E6, [1, 2], [])])]),
        game_tree.TileGameTree(F1, [6, 10], [game_tree.TileGameTree(G1, [1, 3], []),
                                             game_tree.TileGameTree(F2, [3, 3], [
                                                 game_tree.TileGameTree(E2, [3, 3], [
                                                     game_tree.TileGameTree(E3, [1, 2], []),
                                                     game_tree.TileGameTree(D2, [1, 2], [])])]),
                                             game_tree.TileGameTree(D4, [1, 2], [])]),
        game_tree.TileGameTree(D2, [1, 2], []), game_tree.TileGameTree(H7, [1, 2], []),
        game_tree.TileGameTree(B3, [2, 2], [
            game_tree.TileGameTree(B2, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])])]),
        game_tree.TileGameTree(G6, [1, 2], []),
        game_tree.TileGameTree(H1, [2, 2], [game_tree.TileGameTree(F4, [1, 2], [])])]),
                                            game_tree.TileGameTree(D2, [28, 61], [
                                                game_tree.TileGameTree(D3, [5, 9], [
                                                    game_tree.TileGameTree(D4, [3, 3], [
                                                        game_tree.TileGameTree(E4, [1, 2], []),
                                                        game_tree.TileGameTree(D5, [2, 2], [
                                                            game_tree.TileGameTree(E5, [2, 2], [
                                                                game_tree.TileGameTree(H4, [2, 2], [
                                                                    game_tree.TileGameTree(A2,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(C3, [1, 2], []),
                                                    game_tree.TileGameTree(E3, [1, 2], [])]),
                                                game_tree.TileGameTree(C2, [5, 9], [
                                                    game_tree.TileGameTree(B2, [3, 3], [
                                                        game_tree.TileGameTree(A2, [2, 2], [
                                                            game_tree.TileGameTree(A3, [2, 2], [
                                                                game_tree.TileGameTree(A4, [2, 2], [
                                                                    game_tree.TileGameTree(A5,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   A6,
                                                                                                   [
                                                                                                       2,
                                                                                                       2],
                                                                                                   [
                                                                                                       game_tree.TileGameTree(
                                                                                                           E8,
                                                                                                           [
                                                                                                               1,
                                                                                                               2],
                                                                                                           [])])])])])]),
                                                        game_tree.TileGameTree(B1, [1, 2], [])]),
                                                    game_tree.TileGameTree(A4, [1, 2], []),
                                                    game_tree.TileGameTree(C3, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(E3, [2, 2], [
                                                                game_tree.TileGameTree(F3, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(E2, [2, 11], [
                                                    game_tree.TileGameTree(E1, [2, 2], [
                                                        game_tree.TileGameTree(F1, [2, 2], [
                                                            game_tree.TileGameTree(F2, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(E8, [1, 2], [])]),
                                            game_tree.TileGameTree(C1, [25, 41], [
                                                game_tree.TileGameTree(F4, [2, 2], [
                                                    game_tree.TileGameTree(F5, [2, 2], [
                                                        game_tree.TileGameTree(F6, [2, 2], [
                                                            game_tree.TileGameTree(G6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C2, [6, 11], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(D4, [2, 2], [
                                                                game_tree.TileGameTree(C4, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(C3, [2, 4], [
                                                        game_tree.TileGameTree(C4, [1, 2], [])]),
                                                    game_tree.TileGameTree(B2, [1, 2], [])]),
                                                game_tree.TileGameTree(B1, [9, 12], [
                                                    game_tree.TileGameTree(B2, [1, 3], []),
                                                    game_tree.TileGameTree(A1, [6, 7], [
                                                        game_tree.TileGameTree(A2, [2, 5], [
                                                            game_tree.TileGameTree(A3, [2, 2], [
                                                                game_tree.TileGameTree(A4, [2, 2], [
                                                                    game_tree.TileGameTree(A5,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   B5,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])]),
                                                        game_tree.TileGameTree(B3, [1, 2], [])])]),
                                                game_tree.TileGameTree(F7, [1, 2], []),
                                                game_tree.TileGameTree(A2, [1, 2], [])]),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 3], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(B2, [2, 2], [
                                                game_tree.TileGameTree(F3, [1, 2], [])]),
                                            game_tree.TileGameTree(F4, [2, 2], [
                                                game_tree.TileGameTree(F5, [1, 2], [])]),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(F6, [2, 2], [
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(F1, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(C5, [2, 2], [
                                                game_tree.TileGameTree(F4, [1, 2], [])]),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 3], [])]),
    game_tree.TileGameTree(E1, [162, 742], [game_tree.TileGameTree(D1, [22, 36], [
        game_tree.TileGameTree(C1, [10, 13], [game_tree.TileGameTree(B1, [4, 5], [
            game_tree.TileGameTree(B2, [1, 2], []), game_tree.TileGameTree(A1, [1, 3], [])]),
                                              game_tree.TileGameTree(C2, [1, 5], []),
                                              game_tree.TileGameTree(E6, [1, 2], [])]),
        game_tree.TileGameTree(C3, [1, 2], []), game_tree.TileGameTree(A4, [1, 3], []),
        game_tree.TileGameTree(D2, [2, 4], [game_tree.TileGameTree(C2, [1, 2], [])]),
        game_tree.TileGameTree(G4, [1, 2], []), game_tree.TileGameTree(D7, [1, 2], []),
        game_tree.TileGameTree(C8, [1, 2], [])]), game_tree.TileGameTree(F1, [21, 50], [
        game_tree.TileGameTree(F2, [5, 9], [game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(G2, [2, 2], [
                                                game_tree.TileGameTree(G1, [2, 2], [
                                                    game_tree.TileGameTree(H1, [1, 2], [])])]),
                                            game_tree.TileGameTree(F3, [2, 2], [
                                                game_tree.TileGameTree(G3, [1, 2], [])]),
                                            game_tree.TileGameTree(E2, [2, 2], [
                                                game_tree.TileGameTree(A4, [1, 2], [])])]),
        game_tree.TileGameTree(G1, [4, 11], [game_tree.TileGameTree(H1, [2, 3], [
            game_tree.TileGameTree(H2, [2, 2], [game_tree.TileGameTree(H3, [2, 2], [
                game_tree.TileGameTree(H4, [2, 2], [game_tree.TileGameTree(H5, [1, 2], [])])])])]),
                                             game_tree.TileGameTree(G2, [2, 2], [
                                                 game_tree.TileGameTree(H2, [1, 2], [])])]),
        game_tree.TileGameTree(A8, [1, 2], []), game_tree.TileGameTree(G3, [1, 2], [])]),
                                            game_tree.TileGameTree(E2, [15, 34], [
                                                game_tree.TileGameTree(F2, [3, 6], [
                                                    game_tree.TileGameTree(G2, [1, 2], []),
                                                    game_tree.TileGameTree(F1, [2, 2], [
                                                        game_tree.TileGameTree(G1, [1, 2], [])])]),
                                                game_tree.TileGameTree(D2, [1, 5], []),
                                                game_tree.TileGameTree(E3, [3, 4], [
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(F4, [2, 2], [
                                                            game_tree.TileGameTree(F3, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(A6, [1, 2], [])]),
                                                game_tree.TileGameTree(C6, [2, 2], [
                                                    game_tree.TileGameTree(B6, [2, 2], [
                                                        game_tree.TileGameTree(B5, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(C3, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 2], []),
                                            game_tree.TileGameTree(C1, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 3], []),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(G7, [2, 2], []),
                                            game_tree.TileGameTree(E4, [2, 2], [
                                                game_tree.TileGameTree(D7, [2, 2], [
                                                    game_tree.TileGameTree(E8, [2, 2], [])])]),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(D2, [2, 2], [
                                                game_tree.TileGameTree(H4, [1, 2], [])])]),
    game_tree.TileGameTree(F1, [151, 755], [game_tree.TileGameTree(H4, [2, 2], []),
                                            game_tree.TileGameTree(F6, [2, 3], []),
                                            game_tree.TileGameTree(E1, [22, 30], [
                                                game_tree.TileGameTree(H3, [1, 2], []),
                                                game_tree.TileGameTree(E2, [6, 10], [
                                                    game_tree.TileGameTree(F2, [3, 3], [
                                                        game_tree.TileGameTree(G2, [2, 3], [
                                                            game_tree.TileGameTree(H2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E3, [3, 3], [
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(F4, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(D3, [1, 2], [])]),
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(C2, [2, 2], [
                                                            game_tree.TileGameTree(C3, [2, 2], [
                                                                game_tree.TileGameTree(B3, [2, 2], [
                                                                    game_tree.TileGameTree(A3,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   A2,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])])])]),
                                                game_tree.TileGameTree(D1, [5, 9], [
                                                    game_tree.TileGameTree(D2, [1, 3], []),
                                                    game_tree.TileGameTree(C1, [1, 2], []),
                                                    game_tree.TileGameTree(B6, [2, 2], [
                                                        game_tree.TileGameTree(A6, [2, 2], [
                                                            game_tree.TileGameTree(A7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(B4, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], []),
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(A6, [1, 2], [])])]),
                                            game_tree.TileGameTree(G1, [21, 49], [
                                                game_tree.TileGameTree(H1, [1, 10], []),
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(G2, [4, 10], [
                                                    game_tree.TileGameTree(H2, [1, 3], []),
                                                    game_tree.TileGameTree(F2, [2, 2], [
                                                        game_tree.TileGameTree(F3, [2, 2], [
                                                            game_tree.TileGameTree(F4, [2, 2], [
                                                                game_tree.TileGameTree(F5, [2, 2], [
                                                                    game_tree.TileGameTree(G5,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   G6,
                                                                                                   [
                                                                                                       2,
                                                                                                       2],
                                                                                                   [
                                                                                                       game_tree.TileGameTree(
                                                                                                           G7,
                                                                                                           [
                                                                                                               2,
                                                                                                               2],
                                                                                                           [
                                                                                                               game_tree.TileGameTree(
                                                                                                                   G8,
                                                                                                                   [
                                                                                                                       1,
                                                                                                                       2],
                                                                                                                   [])])])])])])])])]),
                                                game_tree.TileGameTree(E5, [2, 2], [
                                                    game_tree.TileGameTree(E6, [1, 2], [])])]),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(F2, [20, 42], [
                                                game_tree.TileGameTree(F3, [5, 7], [
                                                    game_tree.TileGameTree(A4, [1, 2], []),
                                                    game_tree.TileGameTree(F4, [2, 2], [
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(D4, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E3, [1, 2], []),
                                                    game_tree.TileGameTree(G3, [1, 2], [])]),
                                                game_tree.TileGameTree(G2, [1, 7], []),
                                                game_tree.TileGameTree(C1, [1, 2], []),
                                                game_tree.TileGameTree(E2, [3, 6], [
                                                    game_tree.TileGameTree(E1, [2, 3], [
                                                        game_tree.TileGameTree(H7, [1, 2], [])])]),
                                                game_tree.TileGameTree(D6, [1, 2], [])]),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(A8, [2, 3], [
                                                game_tree.TileGameTree(C5, [2, 2], [
                                                    game_tree.TileGameTree(A1, [1, 2], [])])]),
                                            game_tree.TileGameTree(D6, [1, 3], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], [])]),
    game_tree.TileGameTree(G1, [105, 781], [game_tree.TileGameTree(F1, [18, 28], [
        game_tree.TileGameTree(E1, [8, 9], [game_tree.TileGameTree(D1, [3, 4], [
            game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(D3, [2, 2], [
                game_tree.TileGameTree(D4, [2, 2], [game_tree.TileGameTree(C4, [2, 2], [
                    game_tree.TileGameTree(C5, [2, 2], [game_tree.TileGameTree(C6, [2, 2], [
                        game_tree.TileGameTree(C7, [2, 2], [
                            game_tree.TileGameTree(B7, [1, 2], [])])])])])])])]),
            game_tree.TileGameTree(C1, [1, 2], [])]), game_tree.TileGameTree(E2, [2, 4], [
            game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])])]),
                                            game_tree.TileGameTree(D8, [2, 2], [
                                                game_tree.TileGameTree(C8, [2, 2], [
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(C5, [1, 2],
                                                                               [])])])])]),
        game_tree.TileGameTree(F2, [2, 8], [game_tree.TileGameTree(E2, [2, 2], [
            game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(A3, [1, 2], [])])])]),
        game_tree.TileGameTree(G5, [1, 2], []), game_tree.TileGameTree(D8, [1, 2], [])]),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(A6, [1, 3], []),
                                            game_tree.TileGameTree(G2, [20, 31], [
                                                game_tree.TileGameTree(A3, [1, 2], []),
                                                game_tree.TileGameTree(H2, [2, 8], [
                                                    game_tree.TileGameTree(H1, [2, 2], [
                                                        game_tree.TileGameTree(F6, [1, 2], [])])]),
                                                game_tree.TileGameTree(F2, [3, 7], [
                                                    game_tree.TileGameTree(F1, [2, 2], [
                                                        game_tree.TileGameTree(E1, [2, 2], [
                                                            game_tree.TileGameTree(D1, [2, 2], [
                                                                game_tree.TileGameTree(D2, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(F3, [1, 2], [])]),
                                                game_tree.TileGameTree(G3, [5, 6], [
                                                    game_tree.TileGameTree(H3, [1, 3], []),
                                                    game_tree.TileGameTree(A6, [1, 2], []),
                                                    game_tree.TileGameTree(G4, [2, 2], [
                                                        game_tree.TileGameTree(G5, [2, 2], [
                                                            game_tree.TileGameTree(H5, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(H1, [2, 20], [
                                                game_tree.TileGameTree(G8, [1, 2], [])]),
                                            game_tree.TileGameTree(D7, [1, 3], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(E7, [2, 2], [
                                                game_tree.TileGameTree(E6, [2, 2], [
                                                    game_tree.TileGameTree(E5, [1, 2], [])])]),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 3], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(C1, [2, 2], [
                                                game_tree.TileGameTree(F4, [1, 2], [])]),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(F8, [2, 2], [
                                                game_tree.TileGameTree(E7, [2, 2], [])]),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(C5, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 2], [])]),
    game_tree.TileGameTree(H1, [57, 819], [game_tree.TileGameTree(F5, [1, 2], []),
                                           game_tree.TileGameTree(A7, [1, 2], []),
                                           game_tree.TileGameTree(H2, [24, 24], [
                                               game_tree.TileGameTree(G2, [3, 10], [
                                                   game_tree.TileGameTree(F2, [2, 2], [
                                                       game_tree.TileGameTree(E2, [1, 2], [])]),
                                                   game_tree.TileGameTree(G1, [2, 2], [
                                                       game_tree.TileGameTree(F1, [1, 2], [])])]),
                                               game_tree.TileGameTree(H3, [10, 12], [
                                                   game_tree.TileGameTree(H4, [4, 6], [
                                                       game_tree.TileGameTree(G4, [1, 2], []),
                                                       game_tree.TileGameTree(H5, [3, 3], [
                                                           game_tree.TileGameTree(H6, [1, 3],
                                                                                  [])])]),
                                                   game_tree.TileGameTree(G3, [1, 5], [])]),
                                               game_tree.TileGameTree(H8, [1, 2], []),
                                               game_tree.TileGameTree(C7, [1, 2], []),
                                               game_tree.TileGameTree(D5, [1, 2], [])]),
                                           game_tree.TileGameTree(G1, [2, 17], [
                                               game_tree.TileGameTree(G2, [2, 2], [
                                                   game_tree.TileGameTree(G3, [2, 2], [
                                                       game_tree.TileGameTree(H3, [2, 2], [
                                                           game_tree.TileGameTree(H4, [1, 2],
                                                                                  [])])])])]),
                                           game_tree.TileGameTree(A6, [1, 2], []),
                                           game_tree.TileGameTree(D8, [1, 2], []),
                                           game_tree.TileGameTree(G6, [2, 2], [
                                               game_tree.TileGameTree(C2, [1, 2], [])]),
                                           game_tree.TileGameTree(A3, [1, 2], []),
                                           game_tree.TileGameTree(B2, [1, 2], []),
                                           game_tree.TileGameTree(D1, [1, 3], [])]),
    game_tree.TileGameTree(A2, [140, 735], [game_tree.TileGameTree(A1, [11, 30], [
        game_tree.TileGameTree(H1, [1, 2], []), game_tree.TileGameTree(B1, [3, 6], [
            game_tree.TileGameTree(C1, [1, 2], []), game_tree.TileGameTree(B2, [1, 2], [])]),
        game_tree.TileGameTree(A5, [2, 2], [game_tree.TileGameTree(B5, [1, 2], [])]),
        game_tree.TileGameTree(E7, [1, 2], []), game_tree.TileGameTree(H6, [1, 2], []),
        game_tree.TileGameTree(E5, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])])]),
                                            game_tree.TileGameTree(A3, [26, 36], [
                                                game_tree.TileGameTree(B3, [4, 10], [
                                                    game_tree.TileGameTree(B2, [2, 3], [
                                                        game_tree.TileGameTree(C2, [1, 2], [])]),
                                                    game_tree.TileGameTree(C3, [1, 2], [])]),
                                                game_tree.TileGameTree(H5, [1, 2], []),
                                                game_tree.TileGameTree(A4, [8, 12], [
                                                    game_tree.TileGameTree(A5, [5, 7], [
                                                        game_tree.TileGameTree(G3, [1, 2], []),
                                                        game_tree.TileGameTree(B5, [2, 3], [
                                                            game_tree.TileGameTree(B4, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(A6, [1, 2], [])]),
                                                    game_tree.TileGameTree(B4, [1, 2], [])]),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(F1, [1, 2], []),
                                                game_tree.TileGameTree(G5, [1, 2], []),
                                                game_tree.TileGameTree(G4, [1, 2], [])]),
                                            game_tree.TileGameTree(B2, [16, 31], [
                                                game_tree.TileGameTree(B1, [2, 7], [
                                                    game_tree.TileGameTree(C1, [2, 2], [
                                                        game_tree.TileGameTree(D1, [2, 2], [
                                                            game_tree.TileGameTree(D2, [2, 2], [
                                                                game_tree.TileGameTree(C2, [2, 2], [
                                                                    game_tree.TileGameTree(C3,
                                                                                           [1, 2],
                                                                                           [])])])])])]),
                                                game_tree.TileGameTree(C2, [6, 7], [
                                                    game_tree.TileGameTree(C3, [2, 3], [
                                                        game_tree.TileGameTree(D3, [1, 2], [])]),
                                                    game_tree.TileGameTree(C1, [1, 3], []),
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(D1, [1, 2], [])])]),
                                                game_tree.TileGameTree(H7, [1, 3], []),
                                                game_tree.TileGameTree(G1, [1, 2], [])]),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(C3, [2, 2], [
                                                game_tree.TileGameTree(D3, [2, 2], [
                                                    game_tree.TileGameTree(E3, [1, 2], [])])]),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(F4, [2, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(G3, [2, 2], [
                                                game_tree.TileGameTree(H7, [1, 2], [])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(C8, [2, 2], [
                                                game_tree.TileGameTree(H5, [1, 2], [])])]),
    game_tree.TileGameTree(B2, [160, 725], [game_tree.TileGameTree(A2, [11, 30], [
        game_tree.TileGameTree(A1, [1, 6], []), game_tree.TileGameTree(H6, [1, 2], []),
        game_tree.TileGameTree(A3, [2, 4], [game_tree.TileGameTree(B3, [1, 2], [])]),
        game_tree.TileGameTree(D2, [2, 2], [
            game_tree.TileGameTree(C2, [2, 2], [game_tree.TileGameTree(E2, [1, 2], [])])])]),
                                            game_tree.TileGameTree(B3, [22, 32], [
                                                game_tree.TileGameTree(A3, [2, 6], [
                                                    game_tree.TileGameTree(A4, [2, 2], [
                                                        game_tree.TileGameTree(A5, [2, 2], [
                                                            game_tree.TileGameTree(A6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C3, [4, 12], [
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])]),
                                                    game_tree.TileGameTree(C2, [2, 2], [
                                                        game_tree.TileGameTree(D2, [2, 2], [
                                                            game_tree.TileGameTree(E2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D3, [1, 2], [])]),
                                                game_tree.TileGameTree(B4, [5, 5], [
                                                    game_tree.TileGameTree(B5, [2, 3], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])]),
                                                    game_tree.TileGameTree(A4, [1, 2], []),
                                                    game_tree.TileGameTree(B1, [1, 2], [])]),
                                                game_tree.TileGameTree(H5, [1, 2], [])]),
                                            game_tree.TileGameTree(B1, [16, 33], [
                                                game_tree.TileGameTree(A1, [3, 9], [
                                                    game_tree.TileGameTree(A2, [1, 2], []),
                                                    game_tree.TileGameTree(H1, [1, 2], [])]),
                                                game_tree.TileGameTree(C1, [2, 4], [
                                                    game_tree.TileGameTree(D1, [2, 2], [
                                                        game_tree.TileGameTree(D2, [1, 2], [])])]),
                                                game_tree.TileGameTree(F6, [2, 2], []),
                                                game_tree.TileGameTree(H1, [1, 2], []),
                                                game_tree.TileGameTree(B3, [2, 2], [
                                                    game_tree.TileGameTree(G7, [1, 2], [])]),
                                                game_tree.TileGameTree(E8, [1, 2], [])]),
                                            game_tree.TileGameTree(C2, [17, 27], [
                                                game_tree.TileGameTree(C1, [4, 8], [
                                                    game_tree.TileGameTree(B1, [2, 2], [
                                                        game_tree.TileGameTree(D6, [1, 2], [])]),
                                                    game_tree.TileGameTree(D1, [3, 3], [
                                                        game_tree.TileGameTree(D2, [2, 2], [
                                                            game_tree.TileGameTree(F6, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(E1, [1, 2], [])])]),
                                                game_tree.TileGameTree(D2, [3, 5], [
                                                    game_tree.TileGameTree(G6, [1, 2], []),
                                                    game_tree.TileGameTree(D3, [2, 2], [
                                                        game_tree.TileGameTree(C3, [2, 2], [
                                                            game_tree.TileGameTree(B3, [2, 2], [
                                                                game_tree.TileGameTree(B4, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(C3, [2, 4], [
                                                    game_tree.TileGameTree(B3, [2, 2], [
                                                        game_tree.TileGameTree(A3, [1, 2], [])])]),
                                                game_tree.TileGameTree(G3, [1, 2], []),
                                                game_tree.TileGameTree(A6, [1, 2], [])]),
                                            game_tree.TileGameTree(D7, [2, 2], [
                                                game_tree.TileGameTree(D8, [1, 2], [])]),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(C1, [1, 2], []),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(E7, [2, 2], [
                                                game_tree.TileGameTree(A8, [2, 2], [])]),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(F5, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])]),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 3], []),
                                            game_tree.TileGameTree(F4, [2, 2], [
                                                game_tree.TileGameTree(F8, [2, 2], [])])]),
    game_tree.TileGameTree(C2, [191, 704], [game_tree.TileGameTree(C3, [22, 42], [
        game_tree.TileGameTree(B3, [2, 8], [game_tree.TileGameTree(A3, [1, 2], [])]),
        game_tree.TileGameTree(C4, [6, 9], [
            game_tree.TileGameTree(D4, [2, 3], [game_tree.TileGameTree(E4, [1, 2], [])]),
            game_tree.TileGameTree(B4, [2, 3], [game_tree.TileGameTree(B5, [1, 2], [])]),
            game_tree.TileGameTree(C5, [2, 2], [game_tree.TileGameTree(D5, [1, 2], [])])]),
        game_tree.TileGameTree(H5, [1, 3], []),
        game_tree.TileGameTree(D3, [2, 4], [game_tree.TileGameTree(E3, [1, 2], [])]),
        game_tree.TileGameTree(B8, [1, 2], [])]), game_tree.TileGameTree(D2, [16, 28], [
        game_tree.TileGameTree(D3, [2, 6], [game_tree.TileGameTree(D4, [1, 2], [])]),
        game_tree.TileGameTree(D1, [1, 5], []), game_tree.TileGameTree(E2, [3, 5], [
            game_tree.TileGameTree(F2, [1, 2], []), game_tree.TileGameTree(E3, [1, 2], [])]),
        game_tree.TileGameTree(G3, [1, 2], []), game_tree.TileGameTree(A1, [1, 2], [])]),
                                            game_tree.TileGameTree(A6, [1, 3], []),
                                            game_tree.TileGameTree(A1, [2, 3], []),
                                            game_tree.TileGameTree(C1, [15, 40], [
                                                game_tree.TileGameTree(D1, [4, 10], [
                                                    game_tree.TileGameTree(E1, [2, 3], [
                                                        game_tree.TileGameTree(F1, [1, 2], [])]),
                                                    game_tree.TileGameTree(G5, [1, 2], [])]),
                                                game_tree.TileGameTree(B1, [1, 4], []),
                                                game_tree.TileGameTree(A3, [1, 2], []),
                                                game_tree.TileGameTree(H2, [1, 2], [])]),
                                            game_tree.TileGameTree(F5, [2, 2], []),
                                            game_tree.TileGameTree(B2, [16, 30], [
                                                game_tree.TileGameTree(B1, [4, 8], [
                                                    game_tree.TileGameTree(C1, [3, 3], [
                                                        game_tree.TileGameTree(D1, [2, 3], [
                                                            game_tree.TileGameTree(D2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(A1, [1, 2], [])]),
                                                game_tree.TileGameTree(B3, [3, 7], [
                                                    game_tree.TileGameTree(B4, [1, 3], [])]),
                                                game_tree.TileGameTree(A2, [3, 3], [
                                                    game_tree.TileGameTree(A3, [1, 2], []),
                                                    game_tree.TileGameTree(A1, [1, 2], [])])]),
                                            game_tree.TileGameTree(G8, [2, 3], [
                                                game_tree.TileGameTree(D5, [1, 2], [])]),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 4], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(B1, [2, 2], [
                                                game_tree.TileGameTree(A1, [2, 2], [
                                                    game_tree.TileGameTree(H2, [1, 2], [])])]),
                                            game_tree.TileGameTree(E2, [2, 2], [
                                                game_tree.TileGameTree(A1, [1, 2], [])]),
                                            game_tree.TileGameTree(C5, [2, 2], [
                                                game_tree.TileGameTree(C4, [2, 2], [
                                                    game_tree.TileGameTree(D4, [2, 2], [
                                                        game_tree.TileGameTree(F8, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(B4, [2, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], [])]),
    game_tree.TileGameTree(D2, [174, 656], [game_tree.TileGameTree(D1, [20, 41], [
        game_tree.TileGameTree(G3, [1, 2], []),
        game_tree.TileGameTree(B3, [2, 2], [game_tree.TileGameTree(H6, [1, 2], [])]),
        game_tree.TileGameTree(C1, [4, 9], [game_tree.TileGameTree(B1, [2, 3], [
            game_tree.TileGameTree(B2, [2, 2], [
                game_tree.TileGameTree(C2, [2, 2], [game_tree.TileGameTree(C3, [1, 2], [])])])]),
                                            game_tree.TileGameTree(C2, [2, 2], [
                                                game_tree.TileGameTree(C3, [1, 2], [])])]),
        game_tree.TileGameTree(E1, [4, 8], [game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(E2, [1, 2], [])]),
        game_tree.TileGameTree(H6, [2, 2], [game_tree.TileGameTree(H7, [1, 2], [])]),
        game_tree.TileGameTree(C6, [1, 2], [])]), game_tree.TileGameTree(H1, [1, 4], []),
                                            game_tree.TileGameTree(C2, [11, 23], [
                                                game_tree.TileGameTree(C3, [2, 5], [
                                                    game_tree.TileGameTree(D3, [2, 2], [
                                                        game_tree.TileGameTree(E3, [1, 2], [])])]),
                                                game_tree.TileGameTree(C1, [1, 3], []),
                                                game_tree.TileGameTree(B2, [3, 4], [
                                                    game_tree.TileGameTree(B1, [2, 2], [
                                                        game_tree.TileGameTree(C8, [1, 2], [])]),
                                                    game_tree.TileGameTree(B3, [1, 2], [])]),
                                                game_tree.TileGameTree(H4, [1, 2], [])]),
                                            game_tree.TileGameTree(D3, [15, 28], [
                                                game_tree.TileGameTree(D4, [7, 8], [
                                                    game_tree.TileGameTree(D5, [3, 4], [
                                                        game_tree.TileGameTree(D6, [2, 3], [
                                                            game_tree.TileGameTree(C6, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E4, [1, 3], []),
                                                    game_tree.TileGameTree(F1, [1, 2], [])]),
                                                game_tree.TileGameTree(C3, [3, 5], [
                                                    game_tree.TileGameTree(C4, [3, 3], [
                                                        game_tree.TileGameTree(B4, [1, 2], []),
                                                        game_tree.TileGameTree(D4, [2, 2], [
                                                            game_tree.TileGameTree(E4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(E3, [2, 4], [
                                                    game_tree.TileGameTree(F3, [1, 2], [])])]),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(E2, [24, 39], [
                                                game_tree.TileGameTree(E1, [2, 11], [
                                                    game_tree.TileGameTree(G3, [1, 2], [])]),
                                                game_tree.TileGameTree(C4, [1, 2], []),
                                                game_tree.TileGameTree(F2, [3, 6], [
                                                    game_tree.TileGameTree(F1, [2, 2], [
                                                        game_tree.TileGameTree(G1, [1, 2], [])]),
                                                    game_tree.TileGameTree(F3, [1, 2], [])]),
                                                game_tree.TileGameTree(D5, [1, 2], []),
                                                game_tree.TileGameTree(E3, [1, 5], []),
                                                game_tree.TileGameTree(D8, [1, 2], []),
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(B2, [2, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(B5, [2, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(C6, [2, 2], [
                                                game_tree.TileGameTree(D6, [1, 2], [])]),
                                            game_tree.TileGameTree(C7, [1, 2], [])]),
    game_tree.TileGameTree(E2, [189, 666], [game_tree.TileGameTree(C6, [1, 3], []),
                                            game_tree.TileGameTree(E1, [11, 31], [
                                                game_tree.TileGameTree(D1, [4, 6], [
                                                    game_tree.TileGameTree(C1, [2, 4], [
                                                        game_tree.TileGameTree(C2, [1, 2], [])])]),
                                                game_tree.TileGameTree(F1, [2, 4], [
                                                    game_tree.TileGameTree(G1, [2, 2], [
                                                        game_tree.TileGameTree(H1, [1, 2], [])])]),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(C3, [1, 2], [])]),
                                            game_tree.TileGameTree(F2, [20, 40], [
                                                game_tree.TileGameTree(G2, [2, 6], [
                                                    game_tree.TileGameTree(G1, [1, 2], [])]),
                                                game_tree.TileGameTree(F3, [3, 6], [
                                                    game_tree.TileGameTree(E3, [2, 2], [
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(E5, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(F4, [1, 2], [])]),
                                                game_tree.TileGameTree(G5, [1, 2], []),
                                                game_tree.TileGameTree(D5, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], []),
                                                game_tree.TileGameTree(F1, [1, 6], []),
                                                game_tree.TileGameTree(A2, [1, 2], [])]),
                                            game_tree.TileGameTree(D2, [22, 35], [
                                                game_tree.TileGameTree(D3, [4, 8], [
                                                    game_tree.TileGameTree(D4, [2, 3], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])]),
                                                    game_tree.TileGameTree(E3, [2, 2], [
                                                        game_tree.TileGameTree(G6, [1, 2], [])])]),
                                                game_tree.TileGameTree(D1, [2, 6], [
                                                    game_tree.TileGameTree(E1, [2, 2], [
                                                        game_tree.TileGameTree(G3, [1, 2], [])])]),
                                                game_tree.TileGameTree(C2, [7, 9], [
                                                    game_tree.TileGameTree(C3, [1, 3], []),
                                                    game_tree.TileGameTree(E6, [1, 2], []),
                                                    game_tree.TileGameTree(B2, [1, 2], []),
                                                    game_tree.TileGameTree(C1, [1, 3], [])]),
                                                game_tree.TileGameTree(B7, [1, 2], [])]),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(E3, [19, 34], [
                                                game_tree.TileGameTree(D3, [2, 5], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(D1, [1, 2], [])])]),
                                                game_tree.TileGameTree(F3, [1, 5], []),
                                                game_tree.TileGameTree(F4, [1, 2], []),
                                                game_tree.TileGameTree(E4, [5, 6], [
                                                    game_tree.TileGameTree(D4, [2, 4], [
                                                        game_tree.TileGameTree(D3, [1, 2], [])]),
                                                    game_tree.TileGameTree(F3, [1, 2], [])]),
                                                game_tree.TileGameTree(E6, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], []),
                                                game_tree.TileGameTree(D4, [2, 2], [
                                                    game_tree.TileGameTree(D5, [1, 2], [])]),
                                                game_tree.TileGameTree(G8, [1, 2], [])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(E4, [2, 2], [
                                                game_tree.TileGameTree(E5, [2, 2], [
                                                    game_tree.TileGameTree(F7, [1, 2], [])])]),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(G6, [2, 2], [
                                                game_tree.TileGameTree(H6, [1, 2], [])]),
                                            game_tree.TileGameTree(H4, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], [])]),
    game_tree.TileGameTree(F2, [156, 699], [game_tree.TileGameTree(H7, [1, 4], []),
                                            game_tree.TileGameTree(G2, [8, 31], [
                                                game_tree.TileGameTree(G1, [1, 2], []),
                                                game_tree.TileGameTree(B8, [1, 2], []),
                                                game_tree.TileGameTree(G3, [1, 4], []),
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(A6, [2, 2], [
                                                        game_tree.TileGameTree(A5, [1, 2], [])])]),
                                                game_tree.TileGameTree(H2, [1, 2], [])]),
                                            game_tree.TileGameTree(F3, [20, 36], [
                                                game_tree.TileGameTree(E3, [3, 3], [
                                                    game_tree.TileGameTree(E4, [3, 3], [
                                                        game_tree.TileGameTree(D4, [1, 2], []),
                                                        game_tree.TileGameTree(E5, [2, 2], [
                                                            game_tree.TileGameTree(F5, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(E2, [2, 2], [
                                                    game_tree.TileGameTree(C8, [2, 2], [])]),
                                                game_tree.TileGameTree(F4, [8, 9], [
                                                    game_tree.TileGameTree(F5, [1, 4], []),
                                                    game_tree.TileGameTree(E4, [1, 3], []),
                                                    game_tree.TileGameTree(G4, [1, 3], [])]),
                                                game_tree.TileGameTree(G3, [2, 7], [
                                                    game_tree.TileGameTree(H3, [1, 2], [])]),
                                                game_tree.TileGameTree(B5, [2, 2], [
                                                    game_tree.TileGameTree(C5, [1, 2], [])]),
                                                game_tree.TileGameTree(F7, [1, 2], [])]),
                                            game_tree.TileGameTree(F1, [11, 24], [
                                                game_tree.TileGameTree(G1, [1, 5], []),
                                                game_tree.TileGameTree(H7, [1, 2], []),
                                                game_tree.TileGameTree(E1, [4, 5], [
                                                    game_tree.TileGameTree(D1, [1, 2], []),
                                                    game_tree.TileGameTree(E2, [3, 3], [
                                                        game_tree.TileGameTree(D2, [1, 2], []),
                                                        game_tree.TileGameTree(E3, [1, 2], [])])]),
                                                game_tree.TileGameTree(D1, [1, 2], [])]),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(E2, [17, 26], [
                                                game_tree.TileGameTree(E1, [1, 4], []),
                                                game_tree.TileGameTree(D2, [8, 8], [
                                                    game_tree.TileGameTree(D1, [1, 3], []),
                                                    game_tree.TileGameTree(D3, [1, 5], []),
                                                    game_tree.TileGameTree(C2, [1, 2], [])]),
                                                game_tree.TileGameTree(E3, [2, 5], [
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(D4, [1, 2], [])])]),
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(C6, [2, 2], [
                                                    game_tree.TileGameTree(B5, [1, 2], [])])]),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(A2, [2, 3], [
                                                game_tree.TileGameTree(B2, [1, 2], [])]),
                                            game_tree.TileGameTree(F6, [1, 2], [])]),
    game_tree.TileGameTree(G2, [135, 721], [game_tree.TileGameTree(H2, [3, 28], [
        game_tree.TileGameTree(H1, [2, 2], [
            game_tree.TileGameTree(G1, [2, 2], [game_tree.TileGameTree(F1, [1, 2], [])])]),
        game_tree.TileGameTree(H3, [2, 2], [game_tree.TileGameTree(H4, [2, 2], [
            game_tree.TileGameTree(H5, [2, 2], [game_tree.TileGameTree(H6, [2, 2], [
                game_tree.TileGameTree(G6, [1, 2], [])])])])])]),
                                            game_tree.TileGameTree(G1, [12, 27], [
                                                game_tree.TileGameTree(A6, [1, 2], []),
                                                game_tree.TileGameTree(H1, [2, 6], [
                                                    game_tree.TileGameTree(H2, [2, 2], [
                                                        game_tree.TileGameTree(H3, [2, 2], [
                                                            game_tree.TileGameTree(H4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D2, [1, 2], []),
                                                game_tree.TileGameTree(F1, [3, 5], [
                                                    game_tree.TileGameTree(F2, [3, 3], [
                                                        game_tree.TileGameTree(E2, [2, 2], [
                                                            game_tree.TileGameTree(E1, [2, 2], [
                                                                game_tree.TileGameTree(D1, [2, 2], [
                                                                    game_tree.TileGameTree(D2,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   C2,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])]),
                                                        game_tree.TileGameTree(F3, [2, 2], [
                                                            game_tree.TileGameTree(E3, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(G3, [23, 27], [
                                                game_tree.TileGameTree(F3, [5, 9], [
                                                    game_tree.TileGameTree(F2, [1, 2], []),
                                                    game_tree.TileGameTree(F4, [3, 4], [
                                                        game_tree.TileGameTree(G4, [2, 2], [
                                                            game_tree.TileGameTree(H4, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(F5, [2, 2], [
                                                            game_tree.TileGameTree(E5, [2, 2], [
                                                                game_tree.TileGameTree(E6, [2, 2], [
                                                                    game_tree.TileGameTree(D6,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   D7,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])])])]),
                                                game_tree.TileGameTree(H3, [3, 9], [
                                                    game_tree.TileGameTree(H2, [1, 2], []),
                                                    game_tree.TileGameTree(H4, [2, 2], [
                                                        game_tree.TileGameTree(G4, [2, 2], [
                                                            game_tree.TileGameTree(F4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(G4, [5, 7], [
                                                    game_tree.TileGameTree(G5, [1, 2], []),
                                                    game_tree.TileGameTree(F4, [1, 4], [])])]),
                                            game_tree.TileGameTree(H4, [1, 3], []),
                                            game_tree.TileGameTree(F2, [10, 17], [
                                                game_tree.TileGameTree(F1, [1, 4], []),
                                                game_tree.TileGameTree(F3, [2, 4], [
                                                    game_tree.TileGameTree(G3, [2, 2], [
                                                        game_tree.TileGameTree(G4, [2, 2], [
                                                            game_tree.TileGameTree(H4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(E2, [4, 4], [
                                                    game_tree.TileGameTree(E3, [1, 2], []),
                                                    game_tree.TileGameTree(D2, [1, 2], []),
                                                    game_tree.TileGameTree(E1, [1, 2], [])])]),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(C5, [1, 2], []),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(E2, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(A5, [2, 2], [
                                                game_tree.TileGameTree(A7, [1, 2], [])]),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(C1, [2, 3], [
                                                game_tree.TileGameTree(B1, [2, 2], [
                                                    game_tree.TileGameTree(B8, [1, 2], [])])])]),
    game_tree.TileGameTree(H2, [91, 779], [game_tree.TileGameTree(H3, [14, 15], [
        game_tree.TileGameTree(G3, [1, 6], []), game_tree.TileGameTree(H4, [7, 8], [
            game_tree.TileGameTree(G4, [3, 3], [
                game_tree.TileGameTree(G5, [2, 3], [game_tree.TileGameTree(H5, [1, 2], [])])]),
            game_tree.TileGameTree(H5, [3, 4], [game_tree.TileGameTree(H6, [1, 3], [])]),
            game_tree.TileGameTree(A4, [1, 2], [])]), game_tree.TileGameTree(E4, [1, 2], [])]),
                                           game_tree.TileGameTree(A1, [2, 2], [
                                               game_tree.TileGameTree(B1, [1, 2], [])]),
                                           game_tree.TileGameTree(H1, [11, 23], [
                                               game_tree.TileGameTree(G1, [3, 9], [
                                                   game_tree.TileGameTree(G2, [2, 2], [
                                                       game_tree.TileGameTree(F2, [2, 2], [
                                                           game_tree.TileGameTree(F1, [2, 2], [
                                                               game_tree.TileGameTree(D6, [1, 2],
                                                                                      [])])])]),
                                                   game_tree.TileGameTree(F1, [2, 2], [
                                                       game_tree.TileGameTree(F2, [1, 2], [])])]),
                                               game_tree.TileGameTree(G3, [1, 2], []),
                                               game_tree.TileGameTree(B2, [1, 2], [])]),
                                           game_tree.TileGameTree(G6, [1, 2], []),
                                           game_tree.TileGameTree(G2, [5, 25], [
                                               game_tree.TileGameTree(F2, [2, 3], [
                                                   game_tree.TileGameTree(E2, [2, 2], [
                                                       game_tree.TileGameTree(E3, [1, 2], [])])]),
                                               game_tree.TileGameTree(G3, [1, 2], []),
                                               game_tree.TileGameTree(G1, [1, 2], [])]),
                                           game_tree.TileGameTree(H5, [2, 2], [
                                               game_tree.TileGameTree(F2, [1, 2], [])]),
                                           game_tree.TileGameTree(A8, [1, 2], []),
                                           game_tree.TileGameTree(B8, [1, 2], []),
                                           game_tree.TileGameTree(H8, [1, 2], []),
                                           game_tree.TileGameTree(H7, [1, 2], []),
                                           game_tree.TileGameTree(A2, [1, 2], []),
                                           game_tree.TileGameTree(E4, [1, 2], []),
                                           game_tree.TileGameTree(E8, [1, 2], []),
                                           game_tree.TileGameTree(F3, [1, 2], []),
                                           game_tree.TileGameTree(G8, [1, 2], []),
                                           game_tree.TileGameTree(D7, [1, 2], []),
                                           game_tree.TileGameTree(F5, [1, 2], [])]),
    game_tree.TileGameTree(A3, [161, 735], [game_tree.TileGameTree(A4, [26, 42], [
        game_tree.TileGameTree(B7, [1, 2], []), game_tree.TileGameTree(A5, [11, 15], [
            game_tree.TileGameTree(B5, [4, 8], [game_tree.TileGameTree(B4, [1, 3], []),
                                                game_tree.TileGameTree(C5, [1, 2], [])]),
            game_tree.TileGameTree(A6, [3, 4], [game_tree.TileGameTree(A7, [1, 2], []),
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(B4, [1, 2],
                                                                               [])])])])]),
        game_tree.TileGameTree(B4, [3, 10], [game_tree.TileGameTree(B3, [1, 2], []),
                                             game_tree.TileGameTree(C4, [1, 2], [])]),
        game_tree.TileGameTree(F4, [1, 2], [])]), game_tree.TileGameTree(E7, [1, 3], []),
                                            game_tree.TileGameTree(B3, [16, 31], [
                                                game_tree.TileGameTree(B4, [2, 5], [
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(B6, [1, 2], [])])]),
                                                game_tree.TileGameTree(C3, [3, 5], [
                                                    game_tree.TileGameTree(C4, [1, 2], []),
                                                    game_tree.TileGameTree(D3, [2, 2], [
                                                        game_tree.TileGameTree(B7, [1, 2], [])])]),
                                                game_tree.TileGameTree(B2, [3, 8], [
                                                    game_tree.TileGameTree(C2, [2, 2], [
                                                        game_tree.TileGameTree(D2, [1, 2], [])]),
                                                    game_tree.TileGameTree(B1, [1, 2], [])])]),
                                            game_tree.TileGameTree(A2, [20, 38], [
                                                game_tree.TileGameTree(E2, [2, 2], [
                                                    game_tree.TileGameTree(E1, [2, 2], [
                                                        game_tree.TileGameTree(D4, [1, 2], [])])]),
                                                game_tree.TileGameTree(A1, [6, 11], [
                                                    game_tree.TileGameTree(G2, [1, 2], []),
                                                    game_tree.TileGameTree(B7, [1, 2], []),
                                                    game_tree.TileGameTree(H8, [1, 2], []),
                                                    game_tree.TileGameTree(B1, [1, 3], [])]),
                                                game_tree.TileGameTree(H5, [1, 2], []),
                                                game_tree.TileGameTree(B2, [1, 6], []),
                                                game_tree.TileGameTree(G5, [1, 2], []),
                                                game_tree.TileGameTree(A8, [1, 2], [])]),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(H4, [2, 2], []),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], []),
                                            game_tree.TileGameTree(C1, [1, 2], []),
                                            game_tree.TileGameTree(D8, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])]),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(C3, [2, 2], []),
                                            game_tree.TileGameTree(H1, [1, 4], []),
                                            game_tree.TileGameTree(B7, [1, 2], [])]),
    game_tree.TileGameTree(B3, [184, 694], [game_tree.TileGameTree(C3, [20, 32], [
        game_tree.TileGameTree(C4, [4, 9], [game_tree.TileGameTree(D4, [1, 4], [])]),
        game_tree.TileGameTree(C2, [2, 5], [game_tree.TileGameTree(G3, [1, 2], [])]),
        game_tree.TileGameTree(D3, [4, 5], [game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(E3, [2, 2], [
                                                game_tree.TileGameTree(E4, [1, 2], [])]),
                                            game_tree.TileGameTree(D2, [1, 2], [])]),
        game_tree.TileGameTree(A5, [1, 2], []), game_tree.TileGameTree(D7, [1, 2], [])]),
                                            game_tree.TileGameTree(A3, [8, 35], [
                                                game_tree.TileGameTree(A2, [4, 7], [
                                                    game_tree.TileGameTree(B2, [2, 3], [
                                                        game_tree.TileGameTree(B1, [2, 2], [
                                                            game_tree.TileGameTree(A1, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(A1, [2, 2], [
                                                        game_tree.TileGameTree(A4, [2, 2], [
                                                            game_tree.TileGameTree(B4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(H6, [1, 2], [])]),
                                            game_tree.TileGameTree(B4, [18, 35], [
                                                game_tree.TileGameTree(B5, [4, 4], [
                                                    game_tree.TileGameTree(C5, [2, 3], [
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(B6, [2, 2], [
                                                                game_tree.TileGameTree(B7, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(A5, [1, 2], [])]),
                                                game_tree.TileGameTree(A7, [1, 2], []),
                                                game_tree.TileGameTree(G1, [1, 2], []),
                                                game_tree.TileGameTree(A4, [2, 7], [
                                                    game_tree.TileGameTree(A5, [1, 2], [])]),
                                                game_tree.TileGameTree(C4, [1, 5], []),
                                                game_tree.TileGameTree(H4, [2, 2], []),
                                                game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(B2, [19, 33], [
                                                game_tree.TileGameTree(C2, [4, 5], [
                                                    game_tree.TileGameTree(C1, [3, 3], [
                                                        game_tree.TileGameTree(D1, [2, 3], [
                                                            game_tree.TileGameTree(E1, [2, 2], [
                                                                game_tree.TileGameTree(F1, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(E3, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(A2, [2, 7], [
                                                    game_tree.TileGameTree(C8, [2, 2], [
                                                        game_tree.TileGameTree(D8, [1, 2], [])])]),
                                                game_tree.TileGameTree(A5, [1, 2], []),
                                                game_tree.TileGameTree(B1, [4, 7], [
                                                    game_tree.TileGameTree(C1, [1, 2], []),
                                                    game_tree.TileGameTree(A1, [1, 3], [])]),
                                                game_tree.TileGameTree(D7, [1, 2], [])]),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], []),
                                            game_tree.TileGameTree(D6, [1, 3], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(D8, [1, 3], []),
                                            game_tree.TileGameTree(C5, [1, 3], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], [])]),
    game_tree.TileGameTree(C3, [221, 675], [game_tree.TileGameTree(C4, [20, 42], [
        game_tree.TileGameTree(F4, [1, 2], []),
        game_tree.TileGameTree(D4, [2, 6], [game_tree.TileGameTree(A1, [1, 2], [])]),
        game_tree.TileGameTree(B4, [6, 9], [game_tree.TileGameTree(A4, [1, 5], []),
                                            game_tree.TileGameTree(B3, [1, 2], [])]),
        game_tree.TileGameTree(C5, [2, 2], [game_tree.TileGameTree(B5, [1, 2], [])]),
        game_tree.TileGameTree(H6, [1, 2], []), game_tree.TileGameTree(H1, [2, 2], []),
        game_tree.TileGameTree(H4, [1, 2], []), game_tree.TileGameTree(H8, [1, 2], [])]),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(C2, [19, 37], [
                                                game_tree.TileGameTree(C1, [4, 7], [
                                                    game_tree.TileGameTree(B1, [1, 2], []),
                                                    game_tree.TileGameTree(D1, [2, 3], [
                                                        game_tree.TileGameTree(D2, [2, 2], [
                                                            game_tree.TileGameTree(E2, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(A8, [1, 2], []),
                                                game_tree.TileGameTree(B2, [2, 4], [
                                                    game_tree.TileGameTree(B1, [1, 2], [])]),
                                                game_tree.TileGameTree(D2, [3, 6], [
                                                    game_tree.TileGameTree(E2, [1, 2], []),
                                                    game_tree.TileGameTree(D3, [2, 2], [
                                                        game_tree.TileGameTree(D4, [1, 2], [])])]),
                                                game_tree.TileGameTree(H3, [1, 2], []),
                                                game_tree.TileGameTree(E6, [1, 2], []),
                                                game_tree.TileGameTree(G3, [1, 2], [])]),
                                            game_tree.TileGameTree(B3, [21, 40], [
                                                game_tree.TileGameTree(A3, [6, 11], [
                                                    game_tree.TileGameTree(D5, [1, 2], []),
                                                    game_tree.TileGameTree(A2, [2, 4], [
                                                        game_tree.TileGameTree(B2, [2, 2], [
                                                            game_tree.TileGameTree(B1, [2, 2], [
                                                                game_tree.TileGameTree(A1, [2, 2], [
                                                                    game_tree.TileGameTree(C5,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(A4, [1, 2], [])]),
                                                game_tree.TileGameTree(B4, [2, 8], [
                                                    game_tree.TileGameTree(C4, [1, 2], [])]),
                                                game_tree.TileGameTree(D3, [1, 2], []),
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(F5, [1, 2], [])]),
                                            game_tree.TileGameTree(D3, [22, 40], [
                                                game_tree.TileGameTree(E3, [8, 9], [
                                                    game_tree.TileGameTree(E2, [2, 3], [
                                                        game_tree.TileGameTree(F2, [2, 2], [
                                                            game_tree.TileGameTree(G2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E4, [2, 3], [
                                                        game_tree.TileGameTree(E5, [2, 2], [
                                                            game_tree.TileGameTree(E6, [2, 2], [
                                                                game_tree.TileGameTree(D6, [2, 2], [
                                                                    game_tree.TileGameTree(D7,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(F3, [4, 4], [
                                                        game_tree.TileGameTree(F4, [1, 2], []),
                                                        game_tree.TileGameTree(G3, [1, 2], []),
                                                        game_tree.TileGameTree(F2, [2, 2], [
                                                            game_tree.TileGameTree(F1, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D4, [4, 7], [
                                                    game_tree.TileGameTree(C4, [1, 2], []),
                                                    game_tree.TileGameTree(E4, [1, 2], []),
                                                    game_tree.TileGameTree(D5, [1, 2], [])]),
                                                game_tree.TileGameTree(D2, [2, 5], [
                                                    game_tree.TileGameTree(E2, [1, 2], [])]),
                                                game_tree.TileGameTree(D7, [1, 2], []),
                                                game_tree.TileGameTree(A2, [1, 2], []),
                                                game_tree.TileGameTree(F4, [2, 2], [
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(E5, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 5], []),
                                            game_tree.TileGameTree(B6, [1, 3], []),
                                            game_tree.TileGameTree(C8, [1, 3], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 3], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(B5, [2, 3], []),
                                            game_tree.TileGameTree(A2, [2, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(C7, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])])]),
    game_tree.TileGameTree(D3, [211, 663], [game_tree.TileGameTree(E3, [21, 30], [
        game_tree.TileGameTree(F3, [5, 7], [
            game_tree.TileGameTree(F2, [2, 4], [game_tree.TileGameTree(G2, [1, 2], [])]),
            game_tree.TileGameTree(G3, [1, 2], [])]), game_tree.TileGameTree(E4, [3, 4], [
            game_tree.TileGameTree(D4, [2, 2], [game_tree.TileGameTree(C4, [1, 2], [])]),
            game_tree.TileGameTree(E5, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])])]),
        game_tree.TileGameTree(E2, [5, 10], [game_tree.TileGameTree(F2, [1, 2], []),
                                             game_tree.TileGameTree(D2, [2, 2], [
                                                 game_tree.TileGameTree(A8, [1, 2], [])]),
                                             game_tree.TileGameTree(E1, [3, 3], [
                                                 game_tree.TileGameTree(D1, [2, 3], [
                                                     game_tree.TileGameTree(D2, [1, 2], [])])])]),
        game_tree.TileGameTree(E7, [1, 2], []), game_tree.TileGameTree(C6, [1, 2], [])]),
                                            game_tree.TileGameTree(D2, [24, 41], [
                                                game_tree.TileGameTree(E2, [4, 10], [
                                                    game_tree.TileGameTree(F2, [1, 2], []),
                                                    game_tree.TileGameTree(E1, [1, 3], [])]),
                                                game_tree.TileGameTree(D1, [4, 5], [
                                                    game_tree.TileGameTree(C1, [1, 3], []),
                                                    game_tree.TileGameTree(E1, [2, 2], [
                                                        game_tree.TileGameTree(F1, [1, 2], [])])]),
                                                game_tree.TileGameTree(D8, [1, 2], []),
                                                game_tree.TileGameTree(C2, [2, 7], [
                                                    game_tree.TileGameTree(B2, [1, 2], [])]),
                                                game_tree.TileGameTree(B8, [1, 2], []),
                                                game_tree.TileGameTree(C4, [1, 2], []),
                                                game_tree.TileGameTree(A5, [1, 2], [])]),
                                            game_tree.TileGameTree(D4, [23, 42], [
                                                game_tree.TileGameTree(C4, [4, 8], [
                                                    game_tree.TileGameTree(B4, [2, 3], [
                                                        game_tree.TileGameTree(B3, [1, 2], [])]),
                                                    game_tree.TileGameTree(C3, [2, 2], [
                                                        game_tree.TileGameTree(B3, [1, 2], [])])]),
                                                game_tree.TileGameTree(B1, [1, 2], []),
                                                game_tree.TileGameTree(D5, [7, 8], [
                                                    game_tree.TileGameTree(E5, [3, 5], [
                                                        game_tree.TileGameTree(E4, [2, 3], [
                                                            game_tree.TileGameTree(F4, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(F2, [1, 2], []),
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(E6, [1, 2], [])])]),
                                                game_tree.TileGameTree(E4, [5, 8], [
                                                    game_tree.TileGameTree(E5, [1, 2], []),
                                                    game_tree.TileGameTree(F4, [3, 4], [
                                                        game_tree.TileGameTree(F3, [1, 2], []),
                                                        game_tree.TileGameTree(E1, [2, 2], [
                                                            game_tree.TileGameTree(D1, [2, 2], [
                                                                game_tree.TileGameTree(F1, [1, 2],
                                                                                       [])])])])])]),
                                            game_tree.TileGameTree(B5, [1, 3], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(C3, [24, 47], [
                                                game_tree.TileGameTree(C4, [5, 9], [
                                                    game_tree.TileGameTree(B4, [2, 3], [
                                                        game_tree.TileGameTree(B3, [2, 2], [
                                                            game_tree.TileGameTree(B2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C5, [3, 3], [
                                                        game_tree.TileGameTree(B5, [1, 2], []),
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(D6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C2, [3, 7], [
                                                    game_tree.TileGameTree(C1, [1, 2], []),
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(D1, [1, 2], [])])]),
                                                game_tree.TileGameTree(B3, [6, 8], [
                                                    game_tree.TileGameTree(A3, [2, 4], [
                                                        game_tree.TileGameTree(F8, [1, 2], [])]),
                                                    game_tree.TileGameTree(B4, [1, 3], [])]),
                                                game_tree.TileGameTree(A1, [2, 2], [
                                                    game_tree.TileGameTree(E1, [1, 2], [])]),
                                                game_tree.TileGameTree(H5, [1, 2], [])]),
                                            game_tree.TileGameTree(E2, [1, 2], []),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(F4, [2, 4], [
                                                game_tree.TileGameTree(F5, [1, 2], [])]),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(G7, [2, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(E1, [2, 2], [
                                                game_tree.TileGameTree(D1, [2, 2], [
                                                    game_tree.TileGameTree(E4, [1, 2], [])])]),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(G3, [2, 2], [
                                                game_tree.TileGameTree(G8, [1, 2], [])]),
                                            game_tree.TileGameTree(C6, [2, 2], []),
                                            game_tree.TileGameTree(A1, [2, 3], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(B2, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])])]),
    game_tree.TileGameTree(E3, [215, 693], [game_tree.TileGameTree(D3, [17, 36], [
        game_tree.TileGameTree(C3, [5, 7], [game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(C6, [2, 2], [
                                                game_tree.TileGameTree(D6, [1, 2], [])]),
                                            game_tree.TileGameTree(B3, [2, 2], [
                                                game_tree.TileGameTree(A3, [2, 2], [
                                                    game_tree.TileGameTree(A4, [1, 2], [])])])]),
        game_tree.TileGameTree(D4, [3, 8], [game_tree.TileGameTree(C4, [2, 2], [
            game_tree.TileGameTree(C3, [2, 2], [game_tree.TileGameTree(C2, [1, 2], [])])]),
                                            game_tree.TileGameTree(D5, [2, 2], [
                                                game_tree.TileGameTree(C5, [1, 2], [])])]),
        game_tree.TileGameTree(D2, [2, 4], [
            game_tree.TileGameTree(D1, [2, 2], [game_tree.TileGameTree(C1, [1, 2], [])])])]),
                                            game_tree.TileGameTree(E2, [16, 40], [
                                                game_tree.TileGameTree(D2, [4, 6], [
                                                    game_tree.TileGameTree(C2, [3, 3], [
                                                        game_tree.TileGameTree(B2, [1, 2], []),
                                                        game_tree.TileGameTree(C1, [1, 2], [])]),
                                                    game_tree.TileGameTree(D3, [1, 2], [])]),
                                                game_tree.TileGameTree(E1, [1, 3], []),
                                                game_tree.TileGameTree(F2, [4, 9], [
                                                    game_tree.TileGameTree(G2, [1, 3], []),
                                                    game_tree.TileGameTree(F1, [2, 2], [
                                                        game_tree.TileGameTree(E1, [2, 2], [
                                                            game_tree.TileGameTree(D1, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(F3, [18, 46], [
                                                game_tree.TileGameTree(G3, [4, 7], [
                                                    game_tree.TileGameTree(H3, [2, 3], [
                                                        game_tree.TileGameTree(H4, [2, 2], [
                                                            game_tree.TileGameTree(H5, [2, 2], [
                                                                game_tree.TileGameTree(G5, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(G4, [1, 2], [])]),
                                                game_tree.TileGameTree(F4, [2, 6], [
                                                    game_tree.TileGameTree(F5, [1, 2], [])]),
                                                game_tree.TileGameTree(F2, [2, 6], [
                                                    game_tree.TileGameTree(G2, [1, 2], [])]),
                                                game_tree.TileGameTree(B5, [1, 2], [])]),
                                            game_tree.TileGameTree(E4, [23, 43], [
                                                game_tree.TileGameTree(D4, [3, 9], [
                                                    game_tree.TileGameTree(D3, [3, 3], [
                                                        game_tree.TileGameTree(D2, [1, 3], [])])]),
                                                game_tree.TileGameTree(E5, [8, 10], [
                                                    game_tree.TileGameTree(F5, [1, 2], []),
                                                    game_tree.TileGameTree(E6, [4, 4], [
                                                        game_tree.TileGameTree(D6, [1, 2], []),
                                                        game_tree.TileGameTree(E7, [1, 3], [])]),
                                                    game_tree.TileGameTree(D5, [1, 3], []),
                                                    game_tree.TileGameTree(G1, [1, 2], [])]),
                                                game_tree.TileGameTree(F4, [2, 6], [
                                                    game_tree.TileGameTree(F3, [1, 2], [])])]),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(A8, [2, 3], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(H6, [2, 3], []),
                                            game_tree.TileGameTree(B2, [2, 2], [
                                                game_tree.TileGameTree(B3, [1, 2], [])]),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(C3, [2, 2], [
                                                game_tree.TileGameTree(C4, [1, 2], [])]),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(F7, [2, 2], [
                                                game_tree.TileGameTree(G5, [1, 2], [])]),
                                            game_tree.TileGameTree(A2, [2, 2], []),
                                            game_tree.TileGameTree(E5, [2, 3], [
                                                game_tree.TileGameTree(F8, [1, 2], [])]),
                                            game_tree.TileGameTree(E1, [2, 2], [
                                                game_tree.TileGameTree(F1, [1, 2], [])]),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], [])]),
    game_tree.TileGameTree(F3, [194, 694], [game_tree.TileGameTree(G3, [11, 36], [
        game_tree.TileGameTree(H3, [3, 4], [game_tree.TileGameTree(H2, [2, 2], [
            game_tree.TileGameTree(H1, [2, 2], [game_tree.TileGameTree(G1, [1, 2], [])])]),
                                            game_tree.TileGameTree(G5, [1, 2], [])]),
        game_tree.TileGameTree(G4, [2, 4], [
            game_tree.TileGameTree(G5, [2, 2], [game_tree.TileGameTree(G6, [1, 2], [])])]),
        game_tree.TileGameTree(G2, [1, 5], [])]), game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(E3, [20, 34], [
                                                game_tree.TileGameTree(D3, [7, 9], [
                                                    game_tree.TileGameTree(D4, [1, 2], []),
                                                    game_tree.TileGameTree(C3, [4, 5], [
                                                        game_tree.TileGameTree(B3, [2, 3], [
                                                            game_tree.TileGameTree(B2, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(C4, [1, 2], [])]),
                                                    game_tree.TileGameTree(D2, [1, 2], [])]),
                                                game_tree.TileGameTree(H1, [1, 2], []),
                                                game_tree.TileGameTree(E4, [4, 7], [
                                                    game_tree.TileGameTree(E5, [2, 3], [
                                                        game_tree.TileGameTree(E6, [1, 2], [])]),
                                                    game_tree.TileGameTree(D4, [2, 2], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])])]),
                                                game_tree.TileGameTree(E2, [1, 4], []),
                                                game_tree.TileGameTree(D1, [1, 2], [])]),
                                            game_tree.TileGameTree(F4, [28, 36], [
                                                game_tree.TileGameTree(E6, [2, 2], [
                                                    game_tree.TileGameTree(E5, [1, 2], [])]),
                                                game_tree.TileGameTree(C5, [2, 2], [
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(C8, [1, 2], [])])]),
                                                game_tree.TileGameTree(F5, [9, 10], [
                                                    game_tree.TileGameTree(F6, [3, 6], [
                                                        game_tree.TileGameTree(E6, [1, 2], []),
                                                        game_tree.TileGameTree(F7, [2, 2], [
                                                            game_tree.TileGameTree(F8, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C1, [1, 2], []),
                                                    game_tree.TileGameTree(E5, [1, 3], [])]),
                                                game_tree.TileGameTree(C3, [1, 2], []),
                                                game_tree.TileGameTree(E4, [2, 7], [
                                                    game_tree.TileGameTree(E3, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(C3, [2, 2], [
                                                                game_tree.TileGameTree(C4, [2, 2], [
                                                                    game_tree.TileGameTree(B4,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   B5,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])])])]),
                                                game_tree.TileGameTree(E1, [1, 2], []),
                                                game_tree.TileGameTree(G4, [2, 5], [
                                                    game_tree.TileGameTree(G5, [2, 2], [
                                                        game_tree.TileGameTree(H5, [1, 2], [])])]),
                                                game_tree.TileGameTree(G6, [1, 2], []),
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(B5, [1, 2], [])]),
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(F2, [20, 41], [
                                                game_tree.TileGameTree(G2, [1, 4], []),
                                                game_tree.TileGameTree(F1, [6, 9], [
                                                    game_tree.TileGameTree(E1, [3, 4], [
                                                        game_tree.TileGameTree(E2, [1, 3], [])]),
                                                    game_tree.TileGameTree(A4, [1, 2], []),
                                                    game_tree.TileGameTree(G1, [1, 2], [])]),
                                                game_tree.TileGameTree(E2, [3, 7], [
                                                    game_tree.TileGameTree(E1, [2, 3], [
                                                        game_tree.TileGameTree(D1, [1, 2], [])])]),
                                                game_tree.TileGameTree(D6, [1, 2], [])]),
                                            game_tree.TileGameTree(C6, [2, 2], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(H5, [3, 3], [
                                                game_tree.TileGameTree(H4, [1, 2], []),
                                                game_tree.TileGameTree(H6, [1, 2], [])]),
                                            game_tree.TileGameTree(A8, [2, 3], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(D5, [2, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 3], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(C2, [2, 2], []),
                                            game_tree.TileGameTree(F8, [2, 2], [
                                                game_tree.TileGameTree(G2, [1, 2], [])]),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(G1, [2, 2], [
                                                game_tree.TileGameTree(A3, [2, 2], [])]),
                                            game_tree.TileGameTree(G6, [1, 2], [])]),
    game_tree.TileGameTree(G3, [184, 714], [game_tree.TileGameTree(G2, [31, 42], [
        game_tree.TileGameTree(G1, [4, 10], [game_tree.TileGameTree(H1, [1, 3], []),
                                             game_tree.TileGameTree(F1, [1, 2], [])]),
        game_tree.TileGameTree(H2, [2, 9], [game_tree.TileGameTree(H1, [1, 2], [])]),
        game_tree.TileGameTree(G4, [2, 2], [game_tree.TileGameTree(H4, [1, 2], [])]),
        game_tree.TileGameTree(F2, [4, 9], [game_tree.TileGameTree(E2, [1, 2], []),
                                            game_tree.TileGameTree(F1, [3, 3], [
                                                game_tree.TileGameTree(E1, [1, 3], [])])]),
        game_tree.TileGameTree(E6, [2, 2], [
            game_tree.TileGameTree(D6, [2, 2], [game_tree.TileGameTree(D5, [1, 2], [])])]),
        game_tree.TileGameTree(H1, [1, 2], []), game_tree.TileGameTree(F5, [1, 2], []),
        game_tree.TileGameTree(E1, [1, 2], [])]), game_tree.TileGameTree(F3, [14, 36], [
        game_tree.TileGameTree(F4, [2, 6], [game_tree.TileGameTree(F5, [1, 2], [])]),
        game_tree.TileGameTree(H7, [1, 2], []), game_tree.TileGameTree(F2, [1, 4], []),
        game_tree.TileGameTree(E3, [2, 3], [game_tree.TileGameTree(E4, [1, 2], [])]),
        game_tree.TileGameTree(B7, [1, 2], [])]), game_tree.TileGameTree(H3, [12, 36], [
        game_tree.TileGameTree(H4, [6, 6], [game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(H5, [2, 3], [
                                                game_tree.TileGameTree(H6, [2, 2], [
                                                    game_tree.TileGameTree(G6, [1, 2], [])])]),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(F3, [2, 2], [])]),
        game_tree.TileGameTree(H2, [5, 6], [game_tree.TileGameTree(G2, [1, 4], []),
                                            game_tree.TileGameTree(H1, [2, 2], [
                                                game_tree.TileGameTree(G1, [1, 2], [])])]),
        game_tree.TileGameTree(F5, [1, 2], [])]), game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(G4, [20, 33], [
                                                game_tree.TileGameTree(F4, [3, 9], [
                                                    game_tree.TileGameTree(F5, [2, 3], [
                                                        game_tree.TileGameTree(D3, [1, 2], [])])]),
                                                game_tree.TileGameTree(G5, [3, 7], [
                                                    game_tree.TileGameTree(G6, [1, 3], [])]),
                                                game_tree.TileGameTree(H4, [2, 5], [
                                                    game_tree.TileGameTree(D7, [1, 2], [])]),
                                                game_tree.TileGameTree(B1, [1, 2], [])]),
                                            game_tree.TileGameTree(A5, [1, 3], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 3], []),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(A7, [2, 3], []),
                                            game_tree.TileGameTree(F7, [2, 2], [
                                                game_tree.TileGameTree(E7, [2, 2], [
                                                    game_tree.TileGameTree(C2, [1, 2], [])])])]),
    game_tree.TileGameTree(H3, [132, 761], [game_tree.TileGameTree(H4, [34, 42], [
        game_tree.TileGameTree(H5, [13, 19], [game_tree.TileGameTree(G5, [4, 8], [
            game_tree.TileGameTree(F5, [1, 3], []), game_tree.TileGameTree(G6, [1, 2], [])]),
                                              game_tree.TileGameTree(H6, [3, 5], [
                                                  game_tree.TileGameTree(H7, [1, 3], [])]),
                                              game_tree.TileGameTree(F7, [1, 2], [])]),
        game_tree.TileGameTree(F1, [2, 3], [game_tree.TileGameTree(E1, [1, 2], [])]),
        game_tree.TileGameTree(A2, [1, 2], []), game_tree.TileGameTree(G4, [4, 9], [
            game_tree.TileGameTree(G5, [1, 2], []), game_tree.TileGameTree(F4, [1, 2], []),
            game_tree.TileGameTree(G3, [2, 2], [game_tree.TileGameTree(F3, [1, 2], [])])]),
        game_tree.TileGameTree(C5, [1, 2], []), game_tree.TileGameTree(F2, [1, 2], []),
        game_tree.TileGameTree(C4, [1, 2], []), game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(H2, [23, 33], [
                                                game_tree.TileGameTree(H1, [6, 13], [
                                                    game_tree.TileGameTree(A6, [1, 2], []),
                                                    game_tree.TileGameTree(G1, [1, 4], []),
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])])]),
                                                game_tree.TileGameTree(C8, [1, 2], []),
                                                game_tree.TileGameTree(C7, [2, 2], [
                                                    game_tree.TileGameTree(E5, [1, 2], [])]),
                                                game_tree.TileGameTree(G2, [1, 5], []),
                                                game_tree.TileGameTree(E8, [1, 2], []),
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(A7, [1, 2], [])]),
                                            game_tree.TileGameTree(F6, [1, 3], []),
                                            game_tree.TileGameTree(G3, [7, 27], [
                                                game_tree.TileGameTree(F3, [3, 5], [
                                                    game_tree.TileGameTree(F2, [2, 3], [
                                                        game_tree.TileGameTree(F1, [1, 2], [])])]),
                                                game_tree.TileGameTree(G2, [3, 3], [
                                                    game_tree.TileGameTree(F2, [1, 2], []),
                                                    game_tree.TileGameTree(G1, [1, 2], [])])]),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(F3, [2, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(A7, [2, 2], [
                                                game_tree.TileGameTree(A8, [1, 2], [])])]),
    game_tree.TileGameTree(A4, [180, 720], [game_tree.TileGameTree(A3, [31, 46], [
        game_tree.TileGameTree(A2, [13, 18], [game_tree.TileGameTree(B2, [3, 4], [
            game_tree.TileGameTree(C2, [1, 2], []), game_tree.TileGameTree(E7, [1, 2], [])]),
                                              game_tree.TileGameTree(A1, [6, 10], [
                                                  game_tree.TileGameTree(B1, [3, 6], [
                                                      game_tree.TileGameTree(C1, [2, 2], [
                                                          game_tree.TileGameTree(C2, [1, 2], [])]),
                                                      game_tree.TileGameTree(B2, [1, 2], [])])])]),
        game_tree.TileGameTree(B3, [1, 8], []), game_tree.TileGameTree(H8, [1, 2], []),
        game_tree.TileGameTree(D4, [1, 2], []), game_tree.TileGameTree(H2, [1, 2], []),
        game_tree.TileGameTree(E3, [2, 3], [game_tree.TileGameTree(F3, [2, 2], [
            game_tree.TileGameTree(G3, [2, 2], [game_tree.TileGameTree(H3, [1, 2], [])])])]),
        game_tree.TileGameTree(B7, [1, 2], [])]), game_tree.TileGameTree(B4, [14, 30], [
        game_tree.TileGameTree(B5, [2, 6], [
            game_tree.TileGameTree(B6, [2, 2], [game_tree.TileGameTree(B7, [1, 2], [])])]),
        game_tree.TileGameTree(B3, [2, 4], [
            game_tree.TileGameTree(A3, [2, 2], [game_tree.TileGameTree(A2, [1, 2], [])])]),
        game_tree.TileGameTree(C4, [4, 5], [game_tree.TileGameTree(C5, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(C3, [1, 2], [])]),
        game_tree.TileGameTree(E2, [1, 2], [])]), game_tree.TileGameTree(A5, [34, 52], [
        game_tree.TileGameTree(B4, [2, 3], [game_tree.TileGameTree(C8, [1, 2], [])]),
        game_tree.TileGameTree(A6, [7, 17], [game_tree.TileGameTree(B6, [1, 3], []),
                                             game_tree.TileGameTree(B3, [1, 2], []),
                                             game_tree.TileGameTree(A7, [2, 3], [
                                                 game_tree.TileGameTree(C8, [1, 2], [])]),
                                             game_tree.TileGameTree(A8, [1, 2], [])]),
        game_tree.TileGameTree(B5, [5, 11], [game_tree.TileGameTree(B4, [3, 4], [
            game_tree.TileGameTree(C6, [1, 2], []), game_tree.TileGameTree(B3, [1, 2], [])]),
                                             game_tree.TileGameTree(C5, [1, 2], [])]),
        game_tree.TileGameTree(A8, [1, 2], []), game_tree.TileGameTree(C5, [2, 3], [
            game_tree.TileGameTree(C4, [2, 2], [
                game_tree.TileGameTree(C3, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])])])]),
        game_tree.TileGameTree(D4, [2, 2], [game_tree.TileGameTree(D5, [1, 2], [])]),
        game_tree.TileGameTree(G1, [1, 2], [])]), game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 3], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(F4, [2, 3], []),
                                            game_tree.TileGameTree(C1, [1, 3], []),
                                            game_tree.TileGameTree(F5, [2, 2], [
                                                game_tree.TileGameTree(E5, [1, 2], [])]),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(H8, [2, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], [])]),
    game_tree.TileGameTree(B4, [191, 684], [game_tree.TileGameTree(A4, [12, 38], [
        game_tree.TileGameTree(F3, [1, 2], []), game_tree.TileGameTree(A3, [3, 5], [
            game_tree.TileGameTree(A2, [2, 2], [game_tree.TileGameTree(A1, [1, 2], [])]),
            game_tree.TileGameTree(B3, [2, 2], [game_tree.TileGameTree(E7, [1, 2], [])])]),
        game_tree.TileGameTree(B7, [1, 2], []),
        game_tree.TileGameTree(A5, [2, 5], [game_tree.TileGameTree(A6, [1, 2], [])]),
        game_tree.TileGameTree(F6, [1, 2], [])]), game_tree.TileGameTree(B5, [21, 35], [
        game_tree.TileGameTree(F4, [1, 2], []), game_tree.TileGameTree(A5, [1, 8], []),
        game_tree.TileGameTree(B6, [3, 6], [
            game_tree.TileGameTree(B7, [2, 2], [game_tree.TileGameTree(C7, [1, 2], [])]),
            game_tree.TileGameTree(C6, [1, 2], [])]), game_tree.TileGameTree(A1, [1, 2], []),
        game_tree.TileGameTree(D1, [1, 2], []),
        game_tree.TileGameTree(C5, [2, 5], [game_tree.TileGameTree(D5, [1, 2], [])]),
        game_tree.TileGameTree(C1, [1, 2], [])]), game_tree.TileGameTree(B3, [15, 36], [
        game_tree.TileGameTree(A6, [2, 2], []), game_tree.TileGameTree(B2, [7, 8], [
            game_tree.TileGameTree(C2, [1, 2], []), game_tree.TileGameTree(A2, [1, 4], []),
            game_tree.TileGameTree(H3, [1, 2], []), game_tree.TileGameTree(B1, [1, 2], [])]),
        game_tree.TileGameTree(C3, [4, 7], [game_tree.TileGameTree(D3, [2, 2], [
            game_tree.TileGameTree(E3, [2, 2], [game_tree.TileGameTree(D8, [1, 2], [])])]),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], [])])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(C4, [17, 36], [
                                                game_tree.TileGameTree(A3, [1, 2], []),
                                                game_tree.TileGameTree(D4, [3, 5], [
                                                    game_tree.TileGameTree(D5, [1, 2], []),
                                                    game_tree.TileGameTree(F5, [2, 2], [
                                                        game_tree.TileGameTree(F4, [2, 2], [
                                                            game_tree.TileGameTree(A2, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C3, [3, 8], [
                                                    game_tree.TileGameTree(D3, [1, 2], []),
                                                    game_tree.TileGameTree(B3, [2, 2], [
                                                        game_tree.TileGameTree(B2, [1, 2], [])])]),
                                                game_tree.TileGameTree(C5, [1, 3], []),
                                                game_tree.TileGameTree(F1, [2, 2], [
                                                    game_tree.TileGameTree(F2, [2, 2], [
                                                        game_tree.TileGameTree(E2, [1, 2], [])])]),
                                                game_tree.TileGameTree(H2, [1, 2], [])]),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(C3, [1, 2], []),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(A5, [2, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], [])]),
    game_tree.TileGameTree(C4, [227, 665], [game_tree.TileGameTree(C3, [21, 42], [
        game_tree.TileGameTree(C2, [2, 10], [game_tree.TileGameTree(B2, [1, 2], [])]),
        game_tree.TileGameTree(D3, [3, 7], [game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(D4, [2, 2], [
                                                game_tree.TileGameTree(B1, [1, 2], [])])]),
        game_tree.TileGameTree(H2, [1, 2], []), game_tree.TileGameTree(B3, [1, 4], []),
        game_tree.TileGameTree(E3, [1, 2], [])]), game_tree.TileGameTree(D4, [20, 43], [
        game_tree.TileGameTree(D3, [5, 9], [
            game_tree.TileGameTree(E3, [2, 2], [game_tree.TileGameTree(E2, [1, 2], [])]),
            game_tree.TileGameTree(C3, [1, 2], []), game_tree.TileGameTree(G2, [1, 2], []),
            game_tree.TileGameTree(D2, [1, 2], [])]), game_tree.TileGameTree(E4, [6, 6], [
            game_tree.TileGameTree(F4, [1, 3], []), game_tree.TileGameTree(E5, [1, 3], []),
            game_tree.TileGameTree(D8, [1, 2], [])]), game_tree.TileGameTree(D5, [1, 6], []),
        game_tree.TileGameTree(G6, [1, 2], [])]), game_tree.TileGameTree(C5, [29, 48], [
        game_tree.TileGameTree(H6, [1, 2], []), game_tree.TileGameTree(B5, [3, 11], [
            game_tree.TileGameTree(A5, [1, 2], []), game_tree.TileGameTree(B4, [2, 2], [
                game_tree.TileGameTree(B3, [2, 2], [game_tree.TileGameTree(A3, [2, 2], [
                    game_tree.TileGameTree(A2, [2, 2], [game_tree.TileGameTree(A1, [2, 2], [
                        game_tree.TileGameTree(B1, [1, 2], [])])])])])])]),
        game_tree.TileGameTree(C6, [5, 10], [game_tree.TileGameTree(D6, [3, 4], [
            game_tree.TileGameTree(E6, [2, 2], [game_tree.TileGameTree(D2, [1, 2], [])]),
            game_tree.TileGameTree(D7, [1, 2], [])]), game_tree.TileGameTree(C7, [1, 2], [])]),
        game_tree.TileGameTree(D5, [2, 7], [game_tree.TileGameTree(D6, [1, 2], [])]),
        game_tree.TileGameTree(C3, [2, 2], [game_tree.TileGameTree(B3, [1, 2], [])]),
        game_tree.TileGameTree(C8, [1, 2], [])]), game_tree.TileGameTree(B4, [16, 39], [
        game_tree.TileGameTree(A4, [5, 8], [game_tree.TileGameTree(A5, [2, 2], [
            game_tree.TileGameTree(B5, [2, 2], [game_tree.TileGameTree(B6, [2, 2], [
                game_tree.TileGameTree(B7, [2, 2], [game_tree.TileGameTree(B8, [1, 2], [])])])])]),
                                            game_tree.TileGameTree(A3, [4, 4], [
                                                game_tree.TileGameTree(A2, [2, 2], [
                                                    game_tree.TileGameTree(A1, [2, 2], [
                                                        game_tree.TileGameTree(B1, [1, 2], [])])]),
                                                game_tree.TileGameTree(B3, [2, 3], [
                                                    game_tree.TileGameTree(B2, [2, 2], [
                                                        game_tree.TileGameTree(C2, [1, 2],
                                                                               [])])])])]),
        game_tree.TileGameTree(B5, [2, 4], [game_tree.TileGameTree(A5, [1, 2], [])]),
        game_tree.TileGameTree(B3, [1, 4], []), game_tree.TileGameTree(A2, [1, 2], []),
        game_tree.TileGameTree(H7, [1, 2], [])]), game_tree.TileGameTree(B2, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(D1, [2, 2], [
                                                game_tree.TileGameTree(E1, [1, 2], [])]),
                                            game_tree.TileGameTree(H4, [2, 2], [
                                                game_tree.TileGameTree(B6, [2, 2], [
                                                    game_tree.TileGameTree(A2, [2, 2], [])])]),
                                            game_tree.TileGameTree(F3, [2, 2], [
                                                game_tree.TileGameTree(G3, [1, 2], [])]),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(F2, [2, 2], []),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(G7, [2, 2], []),
                                            game_tree.TileGameTree(C2, [2, 2], [
                                                game_tree.TileGameTree(D2, [1, 2], [])]),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(C7, [2, 2], [
                                                game_tree.TileGameTree(E3, [1, 2], [])]),
                                            game_tree.TileGameTree(F1, [2, 2], [
                                                game_tree.TileGameTree(G2, [1, 2], [])])]),
    game_tree.TileGameTree(D4, [207, 648], [game_tree.TileGameTree(E4, [17, 37], [
        game_tree.TileGameTree(F4, [5, 7], [game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(G4, [2, 2], [
                                                game_tree.TileGameTree(G5, [1, 2], [])]),
                                            game_tree.TileGameTree(F5, [2, 2], [
                                                game_tree.TileGameTree(F6, [1, 2], [])]),
                                            game_tree.TileGameTree(H2, [1, 2], [])]),
        game_tree.TileGameTree(E5, [2, 3], [game_tree.TileGameTree(E6, [1, 2], [])]),
        game_tree.TileGameTree(E3, [3, 9], [
            game_tree.TileGameTree(E2, [2, 3], [game_tree.TileGameTree(D2, [1, 2], [])])])]),
                                            game_tree.TileGameTree(D5, [19, 46], [
                                                game_tree.TileGameTree(C5, [1, 5], []),
                                                game_tree.TileGameTree(E5, [1, 6], []),
                                                game_tree.TileGameTree(D6, [6, 8], [
                                                    game_tree.TileGameTree(C6, [1, 2], []),
                                                    game_tree.TileGameTree(D7, [3, 3], [
                                                        game_tree.TileGameTree(E7, [1, 3], [])]),
                                                    game_tree.TileGameTree(F1, [1, 2], []),
                                                    game_tree.TileGameTree(E6, [1, 2], [])]),
                                                game_tree.TileGameTree(H7, [1, 2], []),
                                                game_tree.TileGameTree(E7, [1, 2], [])]),
                                            game_tree.TileGameTree(D3, [17, 41], [
                                                game_tree.TileGameTree(C3, [4, 9], [
                                                    game_tree.TileGameTree(B3, [2, 3], [
                                                        game_tree.TileGameTree(C8, [1, 2], [])]),
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])])]),
                                                game_tree.TileGameTree(E3, [3, 5], [
                                                    game_tree.TileGameTree(E4, [2, 3], [
                                                        game_tree.TileGameTree(E5, [1, 2], [])])]),
                                                game_tree.TileGameTree(D2, [3, 4], [
                                                    game_tree.TileGameTree(D1, [2, 2], [
                                                        game_tree.TileGameTree(E1, [2, 2], [
                                                            game_tree.TileGameTree(E2, [2, 2], [
                                                                game_tree.TileGameTree(F2, [2, 2], [
                                                                    game_tree.TileGameTree(G2,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(C2, [2, 2], [
                                                        game_tree.TileGameTree(C3, [2, 2], [
                                                            game_tree.TileGameTree(C4, [2, 2], [
                                                                game_tree.TileGameTree(G3, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(F2, [2, 2], [
                                                    game_tree.TileGameTree(F3, [1, 2], [])])]),
                                            game_tree.TileGameTree(C4, [18, 31], [
                                                game_tree.TileGameTree(B4, [5, 8], [
                                                    game_tree.TileGameTree(B3, [1, 3], []),
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(B6, [1, 2], [])]),
                                                    game_tree.TileGameTree(A4, [1, 2], [])]),
                                                game_tree.TileGameTree(C3, [1, 2], []),
                                                game_tree.TileGameTree(D1, [1, 2], []),
                                                game_tree.TileGameTree(F5, [1, 2], []),
                                                game_tree.TileGameTree(C5, [2, 8], [
                                                    game_tree.TileGameTree(C6, [1, 2], [])])]),
                                            game_tree.TileGameTree(B5, [1, 3], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(G7, [1, 2], []),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(H5, [2, 2], [
                                                game_tree.TileGameTree(G5, [1, 2], [])]),
                                            game_tree.TileGameTree(G6, [3, 3], [
                                                game_tree.TileGameTree(H6, [1, 2], [])]),
                                            game_tree.TileGameTree(G8, [2, 2], []),
                                            game_tree.TileGameTree(H7, [1, 3], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 2], [
                                                game_tree.TileGameTree(B3, [2, 2], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(B1, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(D2, [2, 2], [
                                                game_tree.TileGameTree(F2, [1, 2], [])])]),
    game_tree.TileGameTree(E4, [214, 648], [game_tree.TileGameTree(F4, [18, 37], [
        game_tree.TileGameTree(F3, [2, 7], [game_tree.TileGameTree(F2, [2, 2], [
            game_tree.TileGameTree(E2, [2, 2], [game_tree.TileGameTree(E1, [1, 2], [])])])]),
        game_tree.TileGameTree(G4, [1, 4], []), game_tree.TileGameTree(F5, [3, 7], [
            game_tree.TileGameTree(F6, [2, 3], [game_tree.TileGameTree(E6, [1, 2], [])])]),
        game_tree.TileGameTree(D8, [1, 2], []), game_tree.TileGameTree(H8, [1, 2], [])]),
                                            game_tree.TileGameTree(D4, [27, 46], [
                                                game_tree.TileGameTree(D3, [7, 9], [
                                                    game_tree.TileGameTree(E3, [4, 4], [
                                                        game_tree.TileGameTree(E2, [1, 3], []),
                                                        game_tree.TileGameTree(F3, [1, 2], [])]),
                                                    game_tree.TileGameTree(D2, [2, 3], [
                                                        game_tree.TileGameTree(C2, [1, 2], [])]),
                                                    game_tree.TileGameTree(C3, [1, 2], [])]),
                                                game_tree.TileGameTree(C4, [5, 7], [
                                                    game_tree.TileGameTree(C3, [1, 2], []),
                                                    game_tree.TileGameTree(B4, [2, 3], [
                                                        game_tree.TileGameTree(A4, [1, 2], [])]),
                                                    game_tree.TileGameTree(C5, [2, 2], [
                                                        game_tree.TileGameTree(B5, [2, 2], [
                                                            game_tree.TileGameTree(B4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(A5, [1, 2], []),
                                                game_tree.TileGameTree(D5, [3, 10], [
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(C6, [1, 2], [])]),
                                                    game_tree.TileGameTree(C5, [1, 2], [])]),
                                                game_tree.TileGameTree(G7, [1, 2], []),
                                                game_tree.TileGameTree(A2, [1, 2], [])]),
                                            game_tree.TileGameTree(E5, [17, 35], [
                                                game_tree.TileGameTree(F5, [3, 7], [
                                                    game_tree.TileGameTree(F4, [2, 2], [
                                                        game_tree.TileGameTree(G4, [1, 2], [])]),
                                                    game_tree.TileGameTree(G5, [2, 2], [
                                                        game_tree.TileGameTree(E3, [1, 2], [])])]),
                                                game_tree.TileGameTree(E6, [8, 9], [
                                                    game_tree.TileGameTree(E7, [2, 4], [
                                                        game_tree.TileGameTree(E8, [1, 2], [])]),
                                                    game_tree.TileGameTree(F6, [3, 5], [
                                                        game_tree.TileGameTree(G3, [1, 2], []),
                                                        game_tree.TileGameTree(F7, [2, 2], [
                                                            game_tree.TileGameTree(G7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D5, [1, 2], [])]),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(E3, [23, 42], [
                                                game_tree.TileGameTree(E2, [7, 9], [
                                                    game_tree.TileGameTree(E1, [3, 3], [
                                                        game_tree.TileGameTree(D1, [1, 2], []),
                                                        game_tree.TileGameTree(F1, [2, 2], [
                                                            game_tree.TileGameTree(F2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D2, [1, 3], []),
                                                    game_tree.TileGameTree(F2, [1, 2], []),
                                                    game_tree.TileGameTree(D1, [1, 2], [])]),
                                                game_tree.TileGameTree(F3, [3, 6], [
                                                    game_tree.TileGameTree(G3, [1, 2], []),
                                                    game_tree.TileGameTree(F2, [1, 2], [])]),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(D2, [1, 2], []),
                                                game_tree.TileGameTree(D3, [3, 5], [
                                                    game_tree.TileGameTree(D4, [2, 3], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])])]),
                                                game_tree.TileGameTree(H3, [1, 2], []),
                                                game_tree.TileGameTree(H2, [1, 2], [])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(C6, [2, 2], [
                                                game_tree.TileGameTree(H1, [2, 2], [])]),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(F7, [2, 3], [
                                                game_tree.TileGameTree(E7, [2, 2], [
                                                    game_tree.TileGameTree(G8, [1, 2], [])])]),
                                            game_tree.TileGameTree(A5, [1, 4], []),
                                            game_tree.TileGameTree(A1, [1, 3], []),
                                            game_tree.TileGameTree(C2, [2, 3], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(B5, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], [])]),
    game_tree.TileGameTree(F4, [183, 665], [game_tree.TileGameTree(E4, [23, 36], [
        game_tree.TileGameTree(E3, [2, 8], [
            game_tree.TileGameTree(E2, [2, 2], [game_tree.TileGameTree(E1, [1, 2], [])])]),
        game_tree.TileGameTree(E5, [2, 6], [game_tree.TileGameTree(D5, [2, 2], [
            game_tree.TileGameTree(D4, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])])])]),
        game_tree.TileGameTree(D4, [8, 8], [game_tree.TileGameTree(D3, [1, 4], []),
                                            game_tree.TileGameTree(C4, [2, 2], [
                                                game_tree.TileGameTree(C5, [2, 2], [
                                                    game_tree.TileGameTree(C6, [1, 2], [])])]),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(C5, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], [])]),
        game_tree.TileGameTree(B6, [1, 2], []), game_tree.TileGameTree(G5, [1, 2], []),
        game_tree.TileGameTree(E7, [2, 2], [])]), game_tree.TileGameTree(F3, [19, 33], [
        game_tree.TileGameTree(F2, [3, 6], [
            game_tree.TileGameTree(G2, [2, 2], [game_tree.TileGameTree(H2, [1, 2], [])]),
            game_tree.TileGameTree(F1, [2, 2], [game_tree.TileGameTree(E1, [1, 2], [])])]),
        game_tree.TileGameTree(E3, [4, 9], [game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(E2, [2, 2], [
                                                game_tree.TileGameTree(F2, [2, 2], [
                                                    game_tree.TileGameTree(G2, [1, 2], [])])])]),
        game_tree.TileGameTree(G3, [1, 5], []), game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(H6, [2, 3], []),
                                            game_tree.TileGameTree(G4, [9, 29], [
                                                game_tree.TileGameTree(G5, [1, 2], []),
                                                game_tree.TileGameTree(G3, [1, 3], []),
                                                game_tree.TileGameTree(H4, [2, 6], [
                                                    game_tree.TileGameTree(H3, [1, 2], [])])]),
                                            game_tree.TileGameTree(F5, [24, 40], [
                                                game_tree.TileGameTree(E5, [2, 5], [
                                                    game_tree.TileGameTree(E6, [2, 2], [
                                                        game_tree.TileGameTree(E7, [1, 2], [])])]),
                                                game_tree.TileGameTree(F6, [7, 11], [
                                                    game_tree.TileGameTree(E6, [2, 5], [
                                                        game_tree.TileGameTree(E5, [1, 2], [])]),
                                                    game_tree.TileGameTree(G6, [1, 3], [])]),
                                                game_tree.TileGameTree(G5, [3, 9], [
                                                    game_tree.TileGameTree(G6, [2, 2], [
                                                        game_tree.TileGameTree(F6, [2, 2], [
                                                            game_tree.TileGameTree(F7, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(G4, [2, 2], [
                                                        game_tree.TileGameTree(G3, [2, 2], [
                                                            game_tree.TileGameTree(F3, [2, 2], [
                                                                game_tree.TileGameTree(F2, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(B1, [1, 2], [])]),
                                            game_tree.TileGameTree(C6, [1, 3], []),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(F8, [1, 3], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(D8, [2, 3], [
                                                game_tree.TileGameTree(C8, [2, 2], [
                                                    game_tree.TileGameTree(G2, [1, 2], [])])]),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(C5, [2, 2], [
                                                game_tree.TileGameTree(F2, [1, 2], [])])]),
    game_tree.TileGameTree(G4, [193, 753], [game_tree.TileGameTree(H4, [7, 42], [
        game_tree.TileGameTree(H5, [4, 5], [
            game_tree.TileGameTree(G5, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])]),
            game_tree.TileGameTree(H6, [1, 2], []), game_tree.TileGameTree(D6, [1, 2], [])]),
        game_tree.TileGameTree(H3, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])]),
        game_tree.TileGameTree(H2, [1, 2], [])]), game_tree.TileGameTree(G5, [14, 30], [
        game_tree.TileGameTree(G6, [3, 3], [game_tree.TileGameTree(F6, [2, 2], [
            game_tree.TileGameTree(E6, [2, 2], [game_tree.TileGameTree(E5, [1, 2], [])])]),
                                            game_tree.TileGameTree(G7, [2, 2], [
                                                game_tree.TileGameTree(G8, [1, 2], [])])]),
        game_tree.TileGameTree(F5, [2, 6], [
            game_tree.TileGameTree(F4, [2, 2], [game_tree.TileGameTree(E4, [1, 2], [])])]),
        game_tree.TileGameTree(G8, [1, 2], []), game_tree.TileGameTree(H5, [1, 5], []),
        game_tree.TileGameTree(G7, [1, 2], [])]), game_tree.TileGameTree(G3, [17, 34], [
        game_tree.TileGameTree(H3, [2, 9], [game_tree.TileGameTree(H2, [2, 2], [
            game_tree.TileGameTree(G2, [2, 2], [game_tree.TileGameTree(F2, [1, 2], [])])])]),
        game_tree.TileGameTree(C6, [2, 2], [game_tree.TileGameTree(B6, [1, 2], [])]),
        game_tree.TileGameTree(F3, [1, 6], []),
        game_tree.TileGameTree(G2, [2, 3], [game_tree.TileGameTree(H1, [1, 2], [])])]),
                                            game_tree.TileGameTree(F4, [13, 43], [
                                                game_tree.TileGameTree(F5, [2, 3], [
                                                    game_tree.TileGameTree(F6, [2, 2], [
                                                        game_tree.TileGameTree(G6, [1, 2], [])])]),
                                                game_tree.TileGameTree(F3, [1, 3], []),
                                                game_tree.TileGameTree(E4, [8, 9], [
                                                    game_tree.TileGameTree(E3, [1, 2], []),
                                                    game_tree.TileGameTree(G5, [1, 2], []),
                                                    game_tree.TileGameTree(D4, [4, 4], [
                                                        game_tree.TileGameTree(C4, [2, 2], [
                                                            game_tree.TileGameTree(C5, [2, 2], [
                                                                game_tree.TileGameTree(B5, [2, 2], [
                                                                    game_tree.TileGameTree(B6,
                                                                                           [1, 2],
                                                                                           [])])])]),
                                                        game_tree.TileGameTree(D3, [2, 3], [
                                                            game_tree.TileGameTree(D2, [2, 2], [
                                                                game_tree.TileGameTree(C2, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(E5, [1, 3], [])])]),
                                            game_tree.TileGameTree(E7, [2, 2], [
                                                game_tree.TileGameTree(D7, [2, 2], [
                                                    game_tree.TileGameTree(D2, [1, 2], [])])]),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 5], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(B2, [1, 2], []),
                                            game_tree.TileGameTree(B5, [2, 2], [
                                                game_tree.TileGameTree(A5, [1, 2], [])]),
                                            game_tree.TileGameTree(D8, [2, 2], [
                                                game_tree.TileGameTree(D7, [1, 2], [])]),
                                            game_tree.TileGameTree(F3, [2, 3], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(H1, [2, 2], [])]),
    game_tree.TileGameTree(H4, [143, 748], [game_tree.TileGameTree(H5, [23, 29], [
        game_tree.TileGameTree(H6, [9, 11], [
            game_tree.TileGameTree(H7, [2, 4], [game_tree.TileGameTree(G7, [1, 2], [])]),
            game_tree.TileGameTree(G6, [2, 5], [game_tree.TileGameTree(F6, [1, 2], [])]),
            game_tree.TileGameTree(H3, [2, 2], [
                game_tree.TileGameTree(H2, [2, 2], [game_tree.TileGameTree(H1, [1, 2], [])])])]),
        game_tree.TileGameTree(G5, [1, 6], []), game_tree.TileGameTree(C5, [1, 2], []),
        game_tree.TileGameTree(D7, [1, 2], []), game_tree.TileGameTree(F8, [1, 2], []),
        game_tree.TileGameTree(A6, [1, 2], []), game_tree.TileGameTree(F1, [1, 2], []),
        game_tree.TileGameTree(H1, [1, 2], []), game_tree.TileGameTree(B1, [1, 2], [])]),
                                            game_tree.TileGameTree(H3, [38, 48], [
                                                game_tree.TileGameTree(G3, [5, 22], [
                                                    game_tree.TileGameTree(G2, [3, 3], [
                                                        game_tree.TileGameTree(G1, [1, 2], []),
                                                        game_tree.TileGameTree(H2, [2, 2], [
                                                            game_tree.TileGameTree(H1, [2, 2], [
                                                                game_tree.TileGameTree(G1, [2, 2], [
                                                                    game_tree.TileGameTree(D5,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(F3, [1, 2], []),
                                                    game_tree.TileGameTree(G4, [1, 2], [])]),
                                                game_tree.TileGameTree(H2, [7, 12], [
                                                    game_tree.TileGameTree(H1, [1, 4], []),
                                                    game_tree.TileGameTree(G2, [1, 4], [])]),
                                                game_tree.TileGameTree(C3, [1, 2], []),
                                                game_tree.TileGameTree(C8, [1, 2], []),
                                                game_tree.TileGameTree(D1, [2, 2], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(E2, [1, 2], [])])]),
                                                game_tree.TileGameTree(B8, [1, 2], []),
                                                game_tree.TileGameTree(C2, [1, 2], [])]),
                                            game_tree.TileGameTree(G4, [8, 30], [
                                                game_tree.TileGameTree(G3, [2, 3], [
                                                    game_tree.TileGameTree(F3, [1, 2], [])]),
                                                game_tree.TileGameTree(F4, [1, 4], []),
                                                game_tree.TileGameTree(F3, [1, 2], []),
                                                game_tree.TileGameTree(G5, [2, 2], [
                                                    game_tree.TileGameTree(H5, [2, 2], [
                                                        game_tree.TileGameTree(H6, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(B5, [1, 2], []),
                                            game_tree.TileGameTree(A4, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])]),
                                            game_tree.TileGameTree(C3, [2, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(E2, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], [])]),
    game_tree.TileGameTree(A5, [169, 719], [game_tree.TileGameTree(A6, [26, 48], [
        game_tree.TileGameTree(A7, [3, 10], [game_tree.TileGameTree(B7, [1, 2], []),
                                             game_tree.TileGameTree(A8, [1, 2], [])]),
        game_tree.TileGameTree(B6, [5, 14], [game_tree.TileGameTree(B7, [1, 2], []),
                                             game_tree.TileGameTree(C6, [1, 3], []),
                                             game_tree.TileGameTree(B5, [2, 2], [
                                                 game_tree.TileGameTree(C5, [1, 2], [])])]),
        game_tree.TileGameTree(B3, [1, 2], []),
        game_tree.TileGameTree(B1, [2, 2], [game_tree.TileGameTree(A1, [1, 2], [])]),
        game_tree.TileGameTree(B2, [2, 2], [game_tree.TileGameTree(A2, [1, 2], [])])]),
                                            game_tree.TileGameTree(B5, [15, 33], [
                                                game_tree.TileGameTree(C5, [5, 8], [
                                                    game_tree.TileGameTree(C4, [1, 2], []),
                                                    game_tree.TileGameTree(C6, [1, 2], []),
                                                    game_tree.TileGameTree(D5, [3, 3], [
                                                        game_tree.TileGameTree(E5, [1, 2], []),
                                                        game_tree.TileGameTree(D6, [1, 2], [])])]),
                                                game_tree.TileGameTree(B4, [5, 6], [
                                                    game_tree.TileGameTree(B3, [2, 4], [
                                                        game_tree.TileGameTree(A3, [1, 2], [])]),
                                                    game_tree.TileGameTree(A4, [2, 2], [
                                                        game_tree.TileGameTree(A3, [1, 2], [])])]),
                                                game_tree.TileGameTree(B6, [3, 3], [
                                                    game_tree.TileGameTree(C6, [3, 3], [
                                                        game_tree.TileGameTree(C7, [1, 2], []),
                                                        game_tree.TileGameTree(D6, [2, 2], [
                                                            game_tree.TileGameTree(D7, [2, 2], [
                                                                game_tree.TileGameTree(C7, [1, 2],
                                                                                       [])])])])])]),
                                            game_tree.TileGameTree(H6, [2, 3], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(A4, [28, 40], [
                                                game_tree.TileGameTree(H7, [1, 2], []),
                                                game_tree.TileGameTree(A3, [8, 12], [
                                                    game_tree.TileGameTree(A2, [3, 6], [
                                                        game_tree.TileGameTree(G8, [2, 2], [
                                                            game_tree.TileGameTree(H8, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(C1, [1, 2], [])]),
                                                    game_tree.TileGameTree(B3, [3, 3], [
                                                        game_tree.TileGameTree(B4, [2, 3], [
                                                            game_tree.TileGameTree(B5, [2, 2], [
                                                                game_tree.TileGameTree(B6, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(B4, [4, 13], [
                                                    game_tree.TileGameTree(B3, [2, 2], [
                                                        game_tree.TileGameTree(B2, [2, 2], [
                                                            game_tree.TileGameTree(C2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(C3, [1, 2], [])]),
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(C5, [2, 2], [
                                                            game_tree.TileGameTree(C4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(B1, [1, 2], []),
                                                game_tree.TileGameTree(C3, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], [])]),
                                            game_tree.TileGameTree(G3, [2, 2], [
                                                game_tree.TileGameTree(G4, [1, 2], [])]),
                                            game_tree.TileGameTree(G6, [1, 3], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(D2, [2, 2], []),
                                            game_tree.TileGameTree(G2, [2, 3], []),
                                            game_tree.TileGameTree(C5, [2, 3], [
                                                game_tree.TileGameTree(H6, [2, 2], [
                                                    game_tree.TileGameTree(H5, [2, 2], [
                                                        game_tree.TileGameTree(G5, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(E3, [2, 2], [
                                                game_tree.TileGameTree(F8, [1, 2], [])])]),
    game_tree.TileGameTree(B5, [207, 690], [game_tree.TileGameTree(B4, [28, 44], [
        game_tree.TileGameTree(C4, [2, 6], [game_tree.TileGameTree(C5, [2, 2], [
            game_tree.TileGameTree(C6, [2, 2], [
                game_tree.TileGameTree(B6, [2, 2], [game_tree.TileGameTree(B7, [1, 2], [])])])])]),
        game_tree.TileGameTree(B3, [3, 8], [game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 2], [])]),
        game_tree.TileGameTree(A4, [5, 12], [game_tree.TileGameTree(E7, [1, 2], []),
                                             game_tree.TileGameTree(A5, [3, 3], [
                                                 game_tree.TileGameTree(A6, [1, 3], [])]),
                                             game_tree.TileGameTree(A3, [2, 2], [
                                                 game_tree.TileGameTree(A2, [1, 2], [])])]),
        game_tree.TileGameTree(F7, [1, 2], []), game_tree.TileGameTree(A8, [1, 2], []),
        game_tree.TileGameTree(E6, [1, 2], []), game_tree.TileGameTree(E4, [1, 2], [])]),
                                            game_tree.TileGameTree(B6, [17, 34], [
                                                game_tree.TileGameTree(C6, [6, 7], [
                                                    game_tree.TileGameTree(C5, [4, 4], [
                                                        game_tree.TileGameTree(C4, [1, 2], []),
                                                        game_tree.TileGameTree(D5, [1, 3], [])]),
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(D7, [1, 2], [])]),
                                                    game_tree.TileGameTree(E7, [1, 2], [])]),
                                                game_tree.TileGameTree(B7, [3, 6], [
                                                    game_tree.TileGameTree(C3, [1, 2], []),
                                                    game_tree.TileGameTree(B8, [1, 2], [])]),
                                                game_tree.TileGameTree(D4, [1, 2], []),
                                                game_tree.TileGameTree(A6, [2, 4], [
                                                    game_tree.TileGameTree(A7, [1, 2], [])]),
                                                game_tree.TileGameTree(F7, [1, 2], [])]),
                                            game_tree.TileGameTree(A5, [14, 42], [
                                                game_tree.TileGameTree(A6, [2, 6], [
                                                    game_tree.TileGameTree(A7, [1, 2], [])]),
                                                game_tree.TileGameTree(A4, [2, 7], [
                                                    game_tree.TileGameTree(A3, [2, 2], [
                                                        game_tree.TileGameTree(B3, [1, 2], [])])]),
                                                game_tree.TileGameTree(B2, [2, 2], [
                                                    game_tree.TileGameTree(C2, [1, 2], [])]),
                                                game_tree.TileGameTree(B6, [1, 2], [])]),
                                            game_tree.TileGameTree(C5, [24, 41], [
                                                game_tree.TileGameTree(C4, [1, 7], []),
                                                game_tree.TileGameTree(D5, [8, 10], [
                                                    game_tree.TileGameTree(D6, [4, 5], [
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(C7, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(D7, [1, 2], []),
                                                        game_tree.TileGameTree(E6, [2, 2], [
                                                            game_tree.TileGameTree(E7, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E5, [2, 2], [
                                                        game_tree.TileGameTree(E6, [2, 2], [
                                                            game_tree.TileGameTree(D6, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D4, [1, 3], [])]),
                                                game_tree.TileGameTree(C6, [5, 9], [
                                                    game_tree.TileGameTree(D6, [1, 4], []),
                                                    game_tree.TileGameTree(C7, [2, 2], [
                                                        game_tree.TileGameTree(B7, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(C1, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(E4, [2, 2], [
                                                game_tree.TileGameTree(E5, [1, 2], [])]),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(B1, [4, 4], [
                                                game_tree.TileGameTree(H3, [1, 2], []),
                                                game_tree.TileGameTree(C1, [2, 2], [
                                                    game_tree.TileGameTree(E7, [1, 2], [])]),
                                                game_tree.TileGameTree(H1, [2, 2], [])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 3], []),
                                            game_tree.TileGameTree(D7, [2, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 3], []),
                                            game_tree.TileGameTree(C6, [2, 2], [])]),
    game_tree.TileGameTree(C5, [228, 684], [game_tree.TileGameTree(B5, [23, 46], [
        game_tree.TileGameTree(B7, [1, 2], []), game_tree.TileGameTree(A5, [5, 10], [
            game_tree.TileGameTree(A6, [1, 4], []), game_tree.TileGameTree(A4, [2, 2], [
                game_tree.TileGameTree(A3, [2, 2], [game_tree.TileGameTree(A2, [1, 2], [])])])]),
        game_tree.TileGameTree(B6, [3, 8], [game_tree.TileGameTree(A6, [1, 3], [])]),
        game_tree.TileGameTree(B1, [1, 2], []), game_tree.TileGameTree(B4, [4, 4], [
            game_tree.TileGameTree(C4, [3, 4], [game_tree.TileGameTree(D4, [3, 3], [
                game_tree.TileGameTree(D5, [2, 2], [
                    game_tree.TileGameTree(E5, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])])]),
                game_tree.TileGameTree(E4, [2, 2], [game_tree.TileGameTree(E5, [1, 2], [])])])])]),
        game_tree.TileGameTree(G6, [1, 2], [])]), game_tree.TileGameTree(C6, [22, 38], [
        game_tree.TileGameTree(B6, [3, 8], [
            game_tree.TileGameTree(B5, [2, 3], [game_tree.TileGameTree(A5, [1, 2], [])])]),
        game_tree.TileGameTree(E5, [1, 2], []), game_tree.TileGameTree(D6, [5, 8], [
            game_tree.TileGameTree(D5, [2, 3], [game_tree.TileGameTree(E5, [2, 2], [
                game_tree.TileGameTree(F5, [2, 2], [game_tree.TileGameTree(F6, [1, 2], [])])])]),
            game_tree.TileGameTree(D7, [1, 2], []), game_tree.TileGameTree(F7, [1, 2], [])]),
        game_tree.TileGameTree(C7, [5, 7], [game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 3], []),
                                            game_tree.TileGameTree(C8, [1, 2], [])])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(D5, [26, 41], [
                                                game_tree.TileGameTree(D4, [3, 7], [
                                                    game_tree.TileGameTree(C4, [1, 2], []),
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(F4, [2, 2], [
                                                            game_tree.TileGameTree(G4, [2, 2], [
                                                                game_tree.TileGameTree(G3, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(H1, [1, 2], []),
                                                game_tree.TileGameTree(D6, [3, 11], [
                                                    game_tree.TileGameTree(E6, [1, 2], []),
                                                    game_tree.TileGameTree(D7, [2, 2], [
                                                        game_tree.TileGameTree(E7, [1, 2], [])])]),
                                                game_tree.TileGameTree(E2, [1, 2], []),
                                                game_tree.TileGameTree(E5, [5, 7], [
                                                    game_tree.TileGameTree(F5, [3, 3], [
                                                        game_tree.TileGameTree(G5, [2, 3], [
                                                            game_tree.TileGameTree(H5, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E4, [1, 2], []),
                                                    game_tree.TileGameTree(E6, [1, 2], [])]),
                                                game_tree.TileGameTree(D3, [2, 2], [
                                                    game_tree.TileGameTree(A8, [1, 2], [])])]),
                                            game_tree.TileGameTree(C4, [19, 47], [
                                                game_tree.TileGameTree(B4, [1, 6], []),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(D4, [4, 9], [
                                                    game_tree.TileGameTree(E7, [1, 2], []),
                                                    game_tree.TileGameTree(E4, [3, 3], [
                                                        game_tree.TileGameTree(E5, [2, 2], [
                                                            game_tree.TileGameTree(D5, [2, 2], [
                                                                game_tree.TileGameTree(D6, [2, 2], [
                                                                    game_tree.TileGameTree(C6,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   C7,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])]),
                                                        game_tree.TileGameTree(F4, [2, 2], [
                                                            game_tree.TileGameTree(F3, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C3, [4, 5], [
                                                    game_tree.TileGameTree(D3, [2, 4], [
                                                        game_tree.TileGameTree(D2, [2, 2], [
                                                            game_tree.TileGameTree(E2, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(F2, [2, 3], [
                                                game_tree.TileGameTree(A6, [1, 2], [])]),
                                            game_tree.TileGameTree(E2, [3, 5], [
                                                game_tree.TileGameTree(F2, [1, 2], [])]),
                                            game_tree.TileGameTree(D1, [1, 3], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(C1, [2, 2], []),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(C3, [2, 2], [
                                                game_tree.TileGameTree(C2, [2, 2], [
                                                    game_tree.TileGameTree(B7, [1, 2], [])])]),
                                            game_tree.TileGameTree(E8, [2, 2], [
                                                game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(H7, [2, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], [])]),
    game_tree.TileGameTree(D5, [217, 662], [game_tree.TileGameTree(D6, [25, 39], [
        game_tree.TileGameTree(D7, [5, 12], [game_tree.TileGameTree(E7, [2, 3], [
            game_tree.TileGameTree(E6, [2, 2], [game_tree.TileGameTree(B5, [1, 2], [])])]),
                                             game_tree.TileGameTree(D8, [2, 2], [
                                                 game_tree.TileGameTree(E8, [2, 2], [
                                                     game_tree.TileGameTree(F8, [2, 2], [
                                                         game_tree.TileGameTree(F7, [1, 2],
                                                                                [])])])]),
                                             game_tree.TileGameTree(G2, [1, 2], [])]),
        game_tree.TileGameTree(C6, [2, 8], [
            game_tree.TileGameTree(B6, [2, 2], [game_tree.TileGameTree(B7, [1, 2], [])])]),
        game_tree.TileGameTree(E6, [2, 6], [game_tree.TileGameTree(E5, [2, 2], [
            game_tree.TileGameTree(E4, [2, 2], [
                game_tree.TileGameTree(E3, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])])])])]),
        game_tree.TileGameTree(A8, [2, 2], [game_tree.TileGameTree(A6, [1, 2], [])])]),
                                            game_tree.TileGameTree(D4, [19, 31], [
                                                game_tree.TileGameTree(F2, [1, 2], []),
                                                game_tree.TileGameTree(C4, [3, 10], [
                                                    game_tree.TileGameTree(C3, [2, 2], [
                                                        game_tree.TileGameTree(D3, [2, 2], [
                                                            game_tree.TileGameTree(D2, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C5, [2, 2], [
                                                        game_tree.TileGameTree(B5, [1, 2], [])])]),
                                                game_tree.TileGameTree(C7, [1, 2], []),
                                                game_tree.TileGameTree(E4, [2, 4], [
                                                    game_tree.TileGameTree(E5, [2, 2], [
                                                        game_tree.TileGameTree(E6, [2, 2], [
                                                            game_tree.TileGameTree(F6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D3, [2, 3], [
                                                    game_tree.TileGameTree(E3, [1, 2], [])]),
                                                game_tree.TileGameTree(H8, [2, 3], [])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(E5, [27, 47], [
                                                game_tree.TileGameTree(E4, [4, 11], [
                                                    game_tree.TileGameTree(E3, [2, 3], [
                                                        game_tree.TileGameTree(E2, [1, 2], [])]),
                                                    game_tree.TileGameTree(D4, [2, 2], [
                                                        game_tree.TileGameTree(D3, [1, 2], [])])]),
                                                game_tree.TileGameTree(E6, [2, 10], [
                                                    game_tree.TileGameTree(F6, [2, 2], [
                                                        game_tree.TileGameTree(F7, [1, 2], [])])]),
                                                game_tree.TileGameTree(F5, [7, 8], [
                                                    game_tree.TileGameTree(G5, [1, 3], []),
                                                    game_tree.TileGameTree(F4, [3, 4], [
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(E3, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(F3, [1, 2], [])]),
                                                    game_tree.TileGameTree(G2, [1, 2], [])])]),
                                            game_tree.TileGameTree(H7, [2, 2], [
                                                game_tree.TileGameTree(H8, [1, 2], [])]),
                                            game_tree.TileGameTree(C5, [15, 28], [
                                                game_tree.TileGameTree(C6, [3, 7], [
                                                    game_tree.TileGameTree(B6, [2, 2], [
                                                        game_tree.TileGameTree(B7, [1, 2], [])]),
                                                    game_tree.TileGameTree(C7, [2, 2], [
                                                        game_tree.TileGameTree(C8, [1, 2], [])])]),
                                                game_tree.TileGameTree(C4, [2, 6], [
                                                    game_tree.TileGameTree(B4, [2, 2], [
                                                        game_tree.TileGameTree(B3, [2, 2], [
                                                            game_tree.TileGameTree(B2, [2, 2], [
                                                                game_tree.TileGameTree(B1, [2, 2], [
                                                                    game_tree.TileGameTree(A1,
                                                                                           [1, 2],
                                                                                           [])])])])])]),
                                                game_tree.TileGameTree(B5, [3, 4], [
                                                    game_tree.TileGameTree(A5, [2, 2], [
                                                        game_tree.TileGameTree(A6, [1, 2], [])]),
                                                    game_tree.TileGameTree(B6, [1, 2], [])])]),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(B4, [2, 2], [
                                                game_tree.TileGameTree(B5, [2, 2], [
                                                    game_tree.TileGameTree(B2, [2, 2], [
                                                        game_tree.TileGameTree(B3, [2, 2], [
                                                            game_tree.TileGameTree(A3, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 2], []),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 4], []),
                                            game_tree.TileGameTree(A5, [2, 2], [
                                                game_tree.TileGameTree(A7, [1, 2], [])]),
                                            game_tree.TileGameTree(E6, [2, 2], [
                                                game_tree.TileGameTree(E7, [1, 2], [])]),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 3], []),
                                            game_tree.TileGameTree(C8, [1, 3], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(F2, [1, 3], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(A6, [2, 2], [
                                                game_tree.TileGameTree(C3, [1, 2], [])]),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], [])]),
    game_tree.TileGameTree(E5, [217, 653], [game_tree.TileGameTree(E6, [19, 37], [
        game_tree.TileGameTree(E7, [7, 8], [game_tree.TileGameTree(F7, [2, 5], [
            game_tree.TileGameTree(G7, [2, 2], [game_tree.TileGameTree(G6, [1, 2], [])])]),
                                            game_tree.TileGameTree(E8, [1, 3], [])]),
        game_tree.TileGameTree(D6, [3, 6], [game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(D7, [1, 2], [])]),
        game_tree.TileGameTree(F6, [1, 5], []), game_tree.TileGameTree(H2, [2, 2], []),
        game_tree.TileGameTree(D2, [2, 2], [
            game_tree.TileGameTree(D3, [2, 2], [game_tree.TileGameTree(E3, [1, 2], [])])])]),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], []),
                                            game_tree.TileGameTree(D5, [19, 35], [
                                                game_tree.TileGameTree(D6, [4, 6], [
                                                    game_tree.TileGameTree(C6, [3, 3], [
                                                        game_tree.TileGameTree(C7, [1, 2], []),
                                                        game_tree.TileGameTree(F8, [1, 2], [])]),
                                                    game_tree.TileGameTree(D7, [1, 2], [])]),
                                                game_tree.TileGameTree(C5, [5, 6], [
                                                    game_tree.TileGameTree(B5, [3, 5], [
                                                        game_tree.TileGameTree(B6, [1, 3], [])])]),
                                                game_tree.TileGameTree(D4, [4, 8], [
                                                    game_tree.TileGameTree(D3, [2, 3], [
                                                        game_tree.TileGameTree(C3, [1, 2], [])]),
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(F4, [1, 2], [])])]),
                                                game_tree.TileGameTree(C1, [1, 2], [])]),
                                            game_tree.TileGameTree(F5, [13, 40], [
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(G5, [4, 6], [
                                                    game_tree.TileGameTree(A8, [1, 2], []),
                                                    game_tree.TileGameTree(A2, [1, 2], []),
                                                    game_tree.TileGameTree(G4, [1, 2], [])]),
                                                game_tree.TileGameTree(H8, [1, 2], []),
                                                game_tree.TileGameTree(F4, [2, 6], [
                                                    game_tree.TileGameTree(B2, [1, 2], [])])]),
                                            game_tree.TileGameTree(E4, [26, 46], [
                                                game_tree.TileGameTree(D4, [5, 8], [
                                                    game_tree.TileGameTree(D5, [4, 4], [
                                                        game_tree.TileGameTree(D6, [1, 4], [])]),
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(C5, [2, 2], [
                                                            game_tree.TileGameTree(B5, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(A3, [2, 2], [
                                                    game_tree.TileGameTree(A2, [2, 2], [
                                                        game_tree.TileGameTree(A1, [1, 2], [])])]),
                                                game_tree.TileGameTree(E3, [6, 9], [
                                                    game_tree.TileGameTree(F3, [1, 3], []),
                                                    game_tree.TileGameTree(D3, [3, 4], [
                                                        game_tree.TileGameTree(D4, [3, 3], [
                                                            game_tree.TileGameTree(C4, [1, 2], []),
                                                            game_tree.TileGameTree(D5, [2, 2], [
                                                                game_tree.TileGameTree(C5, [2, 2], [
                                                                    game_tree.TileGameTree(B5,
                                                                                           [1, 2],
                                                                                           [])])])])])]),
                                                game_tree.TileGameTree(F4, [1, 5], []),
                                                game_tree.TileGameTree(G3, [1, 2], []),
                                                game_tree.TileGameTree(G6, [1, 3], []),
                                                game_tree.TileGameTree(E1, [2, 2], [
                                                    game_tree.TileGameTree(E7, [1, 2], [])]),
                                                game_tree.TileGameTree(A8, [1, 2], [])]),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(E2, [2, 3], [
                                                game_tree.TileGameTree(F2, [1, 2], [])]),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(D8, [2, 2], [
                                                game_tree.TileGameTree(E8, [2, 2], [
                                                    game_tree.TileGameTree(F8, [2, 2], [
                                                        game_tree.TileGameTree(G8, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(H4, [2, 2], []),
                                            game_tree.TileGameTree(D2, [2, 2], [
                                                game_tree.TileGameTree(C8, [1, 2], [])]),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(E1, [2, 2], [
                                                game_tree.TileGameTree(E2, [2, 2], [
                                                    game_tree.TileGameTree(B1, [1, 2], [])])]),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(G4, [2, 2], [])]),
    game_tree.TileGameTree(F5, [188, 679], [game_tree.TileGameTree(F6, [12, 26], [
        game_tree.TileGameTree(B1, [1, 2], []), game_tree.TileGameTree(F7, [1, 5], []),
        game_tree.TileGameTree(E6, [2, 4], [game_tree.TileGameTree(E7, [1, 2], [])]),
        game_tree.TileGameTree(G6, [2, 4], [
            game_tree.TileGameTree(G5, [2, 2], [game_tree.TileGameTree(H5, [1, 2], [])])])]),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(G5, [15, 34], [
                                                game_tree.TileGameTree(G6, [3, 7], [
                                                    game_tree.TileGameTree(C6, [1, 2], []),
                                                    game_tree.TileGameTree(H6, [1, 2], [])]),
                                                game_tree.TileGameTree(H8, [1, 2], []),
                                                game_tree.TileGameTree(H5, [2, 5], [
                                                    game_tree.TileGameTree(H6, [2, 2], [
                                                        game_tree.TileGameTree(H7, [2, 2], [
                                                            game_tree.TileGameTree(G7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(G4, [1, 2], []),
                                                game_tree.TileGameTree(B3, [1, 2], []),
                                                game_tree.TileGameTree(G8, [1, 2], [])]),
                                            game_tree.TileGameTree(F4, [25, 37], [
                                                game_tree.TileGameTree(E4, [6, 13], [
                                                    game_tree.TileGameTree(D4, [2, 2], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])]),
                                                    game_tree.TileGameTree(E5, [2, 4], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])]),
                                                    game_tree.TileGameTree(E3, [1, 2], [])]),
                                                game_tree.TileGameTree(F3, [6, 7], [
                                                    game_tree.TileGameTree(H6, [1, 2], []),
                                                    game_tree.TileGameTree(F2, [2, 2], [
                                                        game_tree.TileGameTree(E2, [1, 2], [])]),
                                                    game_tree.TileGameTree(E3, [3, 3], [
                                                        game_tree.TileGameTree(E2, [3, 3], [
                                                            game_tree.TileGameTree(D2, [1, 3],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(G3, [1, 2], [])]),
                                                game_tree.TileGameTree(G1, [1, 2], []),
                                                game_tree.TileGameTree(G4, [2, 5], [
                                                    game_tree.TileGameTree(G3, [2, 2], [
                                                        game_tree.TileGameTree(G2, [2, 2], [
                                                            game_tree.TileGameTree(G1, [2, 2], [
                                                                game_tree.TileGameTree(F1, [2, 2], [
                                                                    game_tree.TileGameTree(E1,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   E7,
                                                                                                   [
                                                                                                       1,
                                                                                                       2],
                                                                                                   [])])])])])])]),
                                                game_tree.TileGameTree(B6, [1, 2], [])]),
                                            game_tree.TileGameTree(E5, [23, 42], [
                                                game_tree.TileGameTree(E4, [1, 7], []),
                                                game_tree.TileGameTree(E6, [1, 5], []),
                                                game_tree.TileGameTree(A1, [1, 2], []),
                                                game_tree.TileGameTree(D5, [7, 10], [
                                                    game_tree.TileGameTree(D6, [1, 3], []),
                                                    game_tree.TileGameTree(C5, [2, 4], [
                                                        game_tree.TileGameTree(C6, [1, 2], [])]),
                                                    game_tree.TileGameTree(D4, [1, 2], [])]),
                                                game_tree.TileGameTree(D1, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], [])]),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(B4, [2, 2], [
                                                game_tree.TileGameTree(A4, [2, 2], [
                                                    game_tree.TileGameTree(A3, [1, 2], [])])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(G2, [2, 2], []),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(D7, [2, 2], [
                                                game_tree.TileGameTree(D8, [1, 2], [])]),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], [])]),
    game_tree.TileGameTree(G5, [176, 724], [game_tree.TileGameTree(G6, [20, 28], [
        game_tree.TileGameTree(G7, [3, 11], [game_tree.TileGameTree(H7, [1, 3], [])]),
        game_tree.TileGameTree(F6, [1, 4], []), game_tree.TileGameTree(E8, [1, 2], []),
        game_tree.TileGameTree(H6, [1, 5], []), game_tree.TileGameTree(G8, [1, 2], [])]),
                                            game_tree.TileGameTree(H5, [9, 37], [
                                                game_tree.TileGameTree(H4, [4, 5], [
                                                    game_tree.TileGameTree(H3, [2, 2], [
                                                        game_tree.TileGameTree(G3, [2, 2], [
                                                            game_tree.TileGameTree(G4, [2, 2], [
                                                                game_tree.TileGameTree(F4, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(G4, [2, 3], [
                                                        game_tree.TileGameTree(G3, [1, 2], [])])]),
                                                game_tree.TileGameTree(H6, [4, 5], [
                                                    game_tree.TileGameTree(G6, [2, 4], [
                                                        game_tree.TileGameTree(F6, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(F5, [13, 39], [
                                                game_tree.TileGameTree(F4, [4, 5], [
                                                    game_tree.TileGameTree(E4, [3, 3], [
                                                        game_tree.TileGameTree(E5, [2, 3], [
                                                            game_tree.TileGameTree(D5, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(G4, [1, 2], [])]),
                                                game_tree.TileGameTree(E5, [6, 7], [
                                                    game_tree.TileGameTree(E6, [2, 4], [
                                                        game_tree.TileGameTree(E7, [2, 2], [
                                                            game_tree.TileGameTree(D7, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D5, [2, 2], [
                                                        game_tree.TileGameTree(D6, [1, 2], [])]),
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(E3, [2, 2], [
                                                            game_tree.TileGameTree(F3, [2, 2], [
                                                                game_tree.TileGameTree(F4, [2, 2], [
                                                                    game_tree.TileGameTree(F2,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   F1,
                                                                                                   [
                                                                                                       2,
                                                                                                       2],
                                                                                                   [
                                                                                                       game_tree.TileGameTree(
                                                                                                           G1,
                                                                                                           [
                                                                                                               1,
                                                                                                               2],
                                                                                                           [])])])])])])])]),
                                                game_tree.TileGameTree(F6, [1, 3], [])]),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(G4, [20, 23], [
                                                game_tree.TileGameTree(F4, [3, 10], [
                                                    game_tree.TileGameTree(E4, [3, 3], [
                                                        game_tree.TileGameTree(E3, [2, 2], [
                                                            game_tree.TileGameTree(D3, [2, 2], [
                                                                game_tree.TileGameTree(D4, [2, 2], [
                                                                    game_tree.TileGameTree(D5,
                                                                                           [2, 2], [
                                                                                               game_tree.TileGameTree(
                                                                                                   E5,
                                                                                                   [
                                                                                                       2,
                                                                                                       2],
                                                                                                   [
                                                                                                       game_tree.TileGameTree(
                                                                                                           F5,
                                                                                                           [
                                                                                                               1,
                                                                                                               2],
                                                                                                           [])])])])])]),
                                                        game_tree.TileGameTree(E5, [2, 2], [
                                                            game_tree.TileGameTree(D5, [2, 2], [
                                                                game_tree.TileGameTree(D6, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(G3, [4, 6], [
                                                    game_tree.TileGameTree(F3, [1, 2], []),
                                                    game_tree.TileGameTree(H3, [1, 2], []),
                                                    game_tree.TileGameTree(A4, [1, 2], [])]),
                                                game_tree.TileGameTree(H4, [1, 3], []),
                                                game_tree.TileGameTree(D4, [2, 2], [
                                                    game_tree.TileGameTree(H7, [1, 2], [])]),
                                                game_tree.TileGameTree(H3, [1, 2], []),
                                                game_tree.TileGameTree(A6, [1, 2], [])]),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(G2, [2, 3], [
                                                game_tree.TileGameTree(G3, [2, 2], [
                                                    game_tree.TileGameTree(H1, [1, 2], [])])]),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(B7, [2, 2], [
                                                game_tree.TileGameTree(H4, [2, 2], [])]),
                                            game_tree.TileGameTree(G7, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(C5, [2, 2], [
                                                game_tree.TileGameTree(B5, [2, 2], [
                                                    game_tree.TileGameTree(A5, [2, 2], [
                                                        game_tree.TileGameTree(B4, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(B2, [1, 3], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 2], [
                                                game_tree.TileGameTree(F1, [1, 2], [])]),
                                            game_tree.TileGameTree(G3, [2, 2], [
                                                game_tree.TileGameTree(C3, [1, 2], [])]),
                                            game_tree.TileGameTree(F2, [1, 2], [])]),
    game_tree.TileGameTree(H5, [135, 769], [game_tree.TileGameTree(H4, [26, 33], [
        game_tree.TileGameTree(G4, [3, 8], [game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(F4, [2, 2], [
                                                game_tree.TileGameTree(E4, [2, 2], [
                                                    game_tree.TileGameTree(D4, [2, 2], [
                                                        game_tree.TileGameTree(C4, [2, 2], [
                                                            game_tree.TileGameTree(C3, [1, 2],
                                                                                   [])])])])])]),
        game_tree.TileGameTree(C7, [1, 2], []), game_tree.TileGameTree(H3, [12, 16], [
            game_tree.TileGameTree(H2, [1, 7], []), game_tree.TileGameTree(G3, [1, 5], []),
            game_tree.TileGameTree(B3, [1, 2], [])]), game_tree.TileGameTree(D6, [1, 2], []),
        game_tree.TileGameTree(C2, [2, 2], [game_tree.TileGameTree(H8, [1, 2], [])])]),
                                            game_tree.TileGameTree(G5, [11, 33], [
                                                game_tree.TileGameTree(F5, [2, 5], [
                                                    game_tree.TileGameTree(F4, [1, 2], [])]),
                                                game_tree.TileGameTree(G6, [2, 4], [
                                                    game_tree.TileGameTree(F6, [1, 2], [])]),
                                                game_tree.TileGameTree(H8, [1, 2], []),
                                                game_tree.TileGameTree(G4, [2, 3], [
                                                    game_tree.TileGameTree(F4, [1, 2], [])])]),
                                            game_tree.TileGameTree(H6, [24, 38], [
                                                game_tree.TileGameTree(G6, [6, 13], [
                                                    game_tree.TileGameTree(G5, [1, 2], []),
                                                    game_tree.TileGameTree(G7, [2, 5], [
                                                        game_tree.TileGameTree(G8, [1, 2], [])])]),
                                                game_tree.TileGameTree(H7, [6, 9], [
                                                    game_tree.TileGameTree(G7, [2, 3], [
                                                        game_tree.TileGameTree(G8, [1, 2], [])]),
                                                    game_tree.TileGameTree(H8, [1, 4], [])]),
                                                game_tree.TileGameTree(E2, [1, 2], []),
                                                game_tree.TileGameTree(B8, [1, 2], []),
                                                game_tree.TileGameTree(C3, [1, 2], [])]),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(A3, [2, 3], [
                                                game_tree.TileGameTree(G1, [2, 2], [])]),
                                            game_tree.TileGameTree(F7, [1, 2], [])]),
    game_tree.TileGameTree(A6, [144, 757], [game_tree.TileGameTree(A5, [27, 39], [
        game_tree.TileGameTree(A4, [10, 14], [game_tree.TileGameTree(A3, [4, 7], [
            game_tree.TileGameTree(A2, [2, 2], [
                game_tree.TileGameTree(A1, [2, 2], [game_tree.TileGameTree(B1, [1, 2], [])])]),
            game_tree.TileGameTree(B3, [2, 2], [game_tree.TileGameTree(C3, [1, 2], [])]),
            game_tree.TileGameTree(F8, [1, 2], [])]), game_tree.TileGameTree(B4, [2, 4], [
            game_tree.TileGameTree(C7, [1, 2], [])])]), game_tree.TileGameTree(B5, [2, 10], [
            game_tree.TileGameTree(C5, [2, 2], [
                game_tree.TileGameTree(D5, [2, 2], [game_tree.TileGameTree(D6, [1, 2], [])])])]),
        game_tree.TileGameTree(C4, [2, 2], [game_tree.TileGameTree(B4, [1, 2], [])]),
        game_tree.TileGameTree(A2, [2, 2], [game_tree.TileGameTree(E6, [1, 2], [])]),
        game_tree.TileGameTree(G1, [1, 2], []), game_tree.TileGameTree(B8, [1, 2], [])]),
                                            game_tree.TileGameTree(A7, [11, 27], [
                                                game_tree.TileGameTree(A8, [1, 6], []),
                                                game_tree.TileGameTree(E7, [2, 2], [
                                                    game_tree.TileGameTree(F8, [1, 2], [])]),
                                                game_tree.TileGameTree(H2, [1, 2], []),
                                                game_tree.TileGameTree(B7, [1, 2], []),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(H1, [1, 2], [])]),
                                            game_tree.TileGameTree(A8, [1, 3], []),
                                            game_tree.TileGameTree(B6, [19, 37], [
                                                game_tree.TileGameTree(C6, [6, 9], [
                                                    game_tree.TileGameTree(C5, [1, 4], []),
                                                    game_tree.TileGameTree(C7, [2, 2], [
                                                        game_tree.TileGameTree(D7, [2, 2], [
                                                            game_tree.TileGameTree(E7, [2, 2], [
                                                                game_tree.TileGameTree(E6, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(D6, [1, 2], [])]),
                                                game_tree.TileGameTree(D3, [1, 2], []),
                                                game_tree.TileGameTree(B5, [2, 3], [
                                                    game_tree.TileGameTree(B4, [1, 2], [])]),
                                                game_tree.TileGameTree(B7, [2, 6], [
                                                    game_tree.TileGameTree(A7, [2, 2], [
                                                        game_tree.TileGameTree(H8, [1, 2], [])])]),
                                                game_tree.TileGameTree(E3, [1, 2], []),
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(E6, [2, 2], []),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(G8, [2, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(G7, [2, 3], []),
                                            game_tree.TileGameTree(F2, [1, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(D3, [2, 2], [
                                                game_tree.TileGameTree(D4, [1, 2], [])]),
                                            game_tree.TileGameTree(H2, [1, 2], [])]),
    game_tree.TileGameTree(B6, [160, 700], [game_tree.TileGameTree(B7, [16, 36], [
        game_tree.TileGameTree(E1, [1, 2], []), game_tree.TileGameTree(A7, [1, 5], []),
        game_tree.TileGameTree(B8, [2, 6], [game_tree.TileGameTree(A8, [1, 2], [])]),
        game_tree.TileGameTree(C7, [2, 5], [game_tree.TileGameTree(C6, [1, 2], [])]),
        game_tree.TileGameTree(D3, [1, 2], [])]), game_tree.TileGameTree(B5, [16, 29], [
        game_tree.TileGameTree(B4, [4, 4], [game_tree.TileGameTree(C4, [1, 3], []),
                                            game_tree.TileGameTree(B3, [2, 2], [
                                                game_tree.TileGameTree(C3, [2, 2], [
                                                    game_tree.TileGameTree(D3, [2, 2], [
                                                        game_tree.TileGameTree(D4, [1, 2],
                                                                               [])])])])]),
        game_tree.TileGameTree(A5, [2, 4], [
            game_tree.TileGameTree(A6, [2, 2], [game_tree.TileGameTree(A7, [1, 2], [])])]),
        game_tree.TileGameTree(C5, [4, 9], [game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], [])])]),
                                            game_tree.TileGameTree(C6, [12, 25], [
                                                game_tree.TileGameTree(D6, [5, 5], [
                                                    game_tree.TileGameTree(E6, [2, 2], [
                                                        game_tree.TileGameTree(E7, [2, 2], [
                                                            game_tree.TileGameTree(E8, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(D5, [2, 3], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])]),
                                                    game_tree.TileGameTree(A8, [1, 2], [])]),
                                                game_tree.TileGameTree(C5, [2, 4], [
                                                    game_tree.TileGameTree(D5, [1, 2], [])]),
                                                game_tree.TileGameTree(E1, [1, 2], []),
                                                game_tree.TileGameTree(C7, [2, 3], [
                                                    game_tree.TileGameTree(D7, [1, 2], [])]),
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(A6, [10, 35], [
                                                game_tree.TileGameTree(A5, [4, 6], [
                                                    game_tree.TileGameTree(B5, [2, 2], [
                                                        game_tree.TileGameTree(C5, [2, 2], [
                                                            game_tree.TileGameTree(D5, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(G8, [1, 2], []),
                                                    game_tree.TileGameTree(A4, [2, 2], [
                                                        game_tree.TileGameTree(A3, [1, 2], [])])]),
                                                game_tree.TileGameTree(H4, [1, 2], []),
                                                game_tree.TileGameTree(G7, [1, 2], []),
                                                game_tree.TileGameTree(A7, [1, 2], []),
                                                game_tree.TileGameTree(C1, [1, 2], [])]),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(F6, [2, 2], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(C7, [2, 2], []),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(C4, [1, 2], []),
                                            game_tree.TileGameTree(F4, [2, 2], [
                                                game_tree.TileGameTree(C1, [1, 2], [])]),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(E5, [2, 2], [
                                                game_tree.TileGameTree(D5, [1, 2], [])]),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(B8, [2, 2], [
                                                game_tree.TileGameTree(A8, [2, 2], [
                                                    game_tree.TileGameTree(D2, [1, 2], [])])])]),
    game_tree.TileGameTree(C6, [191, 680], [game_tree.TileGameTree(C5, [21, 33], [
        game_tree.TileGameTree(B5, [2, 10], [
            game_tree.TileGameTree(A5, [2, 2], [game_tree.TileGameTree(A4, [1, 2], [])])]),
        game_tree.TileGameTree(C4, [7, 7], [game_tree.TileGameTree(B4, [1, 3], []),
                                            game_tree.TileGameTree(C3, [3, 4], [
                                                game_tree.TileGameTree(D3, [1, 3], [])]),
                                            game_tree.TileGameTree(D4, [1, 2], [])]),
        game_tree.TileGameTree(D5, [1, 3], []), game_tree.TileGameTree(F5, [1, 2], []),
        game_tree.TileGameTree(E8, [1, 2], []), game_tree.TileGameTree(D7, [1, 2], [])]),
                                            game_tree.TileGameTree(B6, [19, 38], [
                                                game_tree.TileGameTree(B7, [3, 9], [
                                                    game_tree.TileGameTree(B8, [1, 2], []),
                                                    game_tree.TileGameTree(A7, [1, 2], [])]),
                                                game_tree.TileGameTree(B5, [5, 7], [
                                                    game_tree.TileGameTree(A5, [2, 3], [
                                                        game_tree.TileGameTree(A4, [1, 2], [])]),
                                                    game_tree.TileGameTree(B4, [2, 2], [
                                                        game_tree.TileGameTree(A4, [1, 2], [])]),
                                                    game_tree.TileGameTree(C5, [2, 2], [
                                                        game_tree.TileGameTree(C4, [2, 2], [
                                                            game_tree.TileGameTree(D4, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(A6, [2, 4], [
                                                    game_tree.TileGameTree(A5, [1, 2], [])]),
                                                game_tree.TileGameTree(D7, [1, 2], [])]),
                                            game_tree.TileGameTree(D6, [19, 31], [
                                                game_tree.TileGameTree(D7, [1, 6], []),
                                                game_tree.TileGameTree(D5, [3, 7], [
                                                    game_tree.TileGameTree(D4, [3, 3], [
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(F4, [2, 2], [
                                                                game_tree.TileGameTree(F5, [1, 2],
                                                                                       [])])]),
                                                        game_tree.TileGameTree(D3, [1, 2], [])])]),
                                                game_tree.TileGameTree(B4, [1, 2], []),
                                                game_tree.TileGameTree(E6, [4, 5], [
                                                    game_tree.TileGameTree(E7, [1, 2], []),
                                                    game_tree.TileGameTree(A8, [1, 2], []),
                                                    game_tree.TileGameTree(B7, [1, 2], [])]),
                                                game_tree.TileGameTree(G3, [1, 2], []),
                                                game_tree.TileGameTree(H2, [2, 2], [])]),
                                            game_tree.TileGameTree(C7, [13, 38], [
                                                game_tree.TileGameTree(C8, [2, 5], [
                                                    game_tree.TileGameTree(B8, [1, 2], [])]),
                                                game_tree.TileGameTree(D7, [3, 6], [
                                                    game_tree.TileGameTree(E7, [2, 2], [
                                                        game_tree.TileGameTree(F7, [1, 2], [])]),
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])])]),
                                                game_tree.TileGameTree(B7, [1, 3], [])]),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(C4, [3, 3], [
                                                game_tree.TileGameTree(D4, [1, 2], []),
                                                game_tree.TileGameTree(C3, [2, 2], [
                                                    game_tree.TileGameTree(C2, [1, 2], [])])]),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(C3, [1, 2], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(G3, [2, 2], [
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(G7, [1, 2], []),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(A5, [2, 2], [])]),
    game_tree.TileGameTree(D6, [220, 686], [game_tree.TileGameTree(C6, [17, 41], [
        game_tree.TileGameTree(B6, [4, 6], [game_tree.TileGameTree(B5, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], [])]),
        game_tree.TileGameTree(C5, [2, 4], [
            game_tree.TileGameTree(D5, [2, 2], [game_tree.TileGameTree(E5, [1, 2], [])])]),
        game_tree.TileGameTree(C7, [3, 6], [game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], [])]),
        game_tree.TileGameTree(G4, [1, 2], []), game_tree.TileGameTree(H6, [1, 2], []),
        game_tree.TileGameTree(F3, [1, 2], [])]), game_tree.TileGameTree(D7, [10, 31], [
        game_tree.TileGameTree(E7, [1, 5], []), game_tree.TileGameTree(D8, [2, 5], [
            game_tree.TileGameTree(E8, [2, 2], [game_tree.TileGameTree(G6, [1, 2], [])])]),
        game_tree.TileGameTree(C7, [2, 2], [game_tree.TileGameTree(C6, [1, 2], [])])]),
                                            game_tree.TileGameTree(D5, [17, 35], [
                                                game_tree.TileGameTree(F7, [2, 2], [
                                                    game_tree.TileGameTree(F8, [1, 2], [])]),
                                                game_tree.TileGameTree(C5, [1, 5], []),
                                                game_tree.TileGameTree(E5, [4, 6], [
                                                    game_tree.TileGameTree(F5, [2, 3], [
                                                        game_tree.TileGameTree(G5, [2, 2], [
                                                            game_tree.TileGameTree(H5, [2, 2], [
                                                                game_tree.TileGameTree(H6, [2, 2], [
                                                                    game_tree.TileGameTree(H7,
                                                                                           [1, 2],
                                                                                           [])])])])]),
                                                    game_tree.TileGameTree(E6, [1, 2], [])]),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(D4, [5, 6], [
                                                    game_tree.TileGameTree(D3, [2, 4], [
                                                        game_tree.TileGameTree(D2, [1, 2], [])]),
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(F4, [2, 2], [
                                                            game_tree.TileGameTree(F3, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(E6, [33, 52], [
                                                game_tree.TileGameTree(E7, [2, 14], [
                                                    game_tree.TileGameTree(D7, [1, 2], [])]),
                                                game_tree.TileGameTree(F6, [9, 11], [
                                                    game_tree.TileGameTree(G6, [2, 2], [
                                                        game_tree.TileGameTree(G5, [2, 2], [
                                                            game_tree.TileGameTree(G4, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(F7, [2, 4], [
                                                        game_tree.TileGameTree(H7, [1, 2], [])]),
                                                    game_tree.TileGameTree(F5, [1, 5], [])]),
                                                game_tree.TileGameTree(E5, [5, 8], [
                                                    game_tree.TileGameTree(E4, [3, 4], [
                                                        game_tree.TileGameTree(F4, [1, 2], []),
                                                        game_tree.TileGameTree(D4, [1, 2], [])]),
                                                    game_tree.TileGameTree(D5, [2, 2], [
                                                        game_tree.TileGameTree(G8, [1, 2], [])])]),
                                                game_tree.TileGameTree(H5, [1, 2], []),
                                                game_tree.TileGameTree(H1, [2, 2], [
                                                    game_tree.TileGameTree(G1, [1, 2], [])])]),
                                            game_tree.TileGameTree(F6, [1, 4], []),
                                            game_tree.TileGameTree(A3, [2, 3], []),
                                            game_tree.TileGameTree(A4, [2, 2], [
                                                game_tree.TileGameTree(B4, [2, 2], [
                                                    game_tree.TileGameTree(H3, [1, 2], [])])]),
                                            game_tree.TileGameTree(B8, [1, 3], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(D3, [2, 2], [
                                                game_tree.TileGameTree(E3, [1, 2], [])]),
                                            game_tree.TileGameTree(A8, [2, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(G6, [2, 4], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(F7, [2, 2], [
                                                game_tree.TileGameTree(B2, [1, 2], [])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 2], [])]),
    game_tree.TileGameTree(E6, [211, 691], [game_tree.TileGameTree(F6, [22, 42], [
        game_tree.TileGameTree(G5, [1, 2], []), game_tree.TileGameTree(F5, [3, 8], [
            game_tree.TileGameTree(G5, [1, 2], []), game_tree.TileGameTree(E5, [2, 2], [
                game_tree.TileGameTree(E4, [2, 2], [game_tree.TileGameTree(E3, [1, 2], [])])])]),
        game_tree.TileGameTree(G6, [7, 11], [game_tree.TileGameTree(G5, [2, 4], [
            game_tree.TileGameTree(H5, [2, 2], [game_tree.TileGameTree(H6, [1, 2], [])])]),
                                             game_tree.TileGameTree(G7, [1, 2], []),
                                             game_tree.TileGameTree(H6, [1, 3], [])]),
        game_tree.TileGameTree(F7, [2, 3], [game_tree.TileGameTree(G7, [1, 2], [])]),
        game_tree.TileGameTree(A8, [1, 2], [])]), game_tree.TileGameTree(E7, [16, 45], [
        game_tree.TileGameTree(E8, [1, 8], []),
        game_tree.TileGameTree(D7, [2, 5], [game_tree.TileGameTree(D6, [1, 2], [])]),
        game_tree.TileGameTree(F2, [1, 2], []), game_tree.TileGameTree(F7, [1, 3], []),
        game_tree.TileGameTree(H3, [1, 2], [])]), game_tree.TileGameTree(E5, [16, 37], [
        game_tree.TileGameTree(F5, [2, 5], [game_tree.TileGameTree(F4, [2, 2], [
            game_tree.TileGameTree(E4, [2, 2], [game_tree.TileGameTree(E3, [1, 2], [])])])]),
        game_tree.TileGameTree(E4, [8, 9], [
            game_tree.TileGameTree(D4, [2, 3], [game_tree.TileGameTree(D3, [1, 2], [])]),
            game_tree.TileGameTree(E3, [4, 4], [game_tree.TileGameTree(F3, [1, 4], [])]),
            game_tree.TileGameTree(B8, [1, 2], []), game_tree.TileGameTree(F4, [1, 2], [])]),
        game_tree.TileGameTree(D5, [2, 3], [game_tree.TileGameTree(D6, [1, 2], [])]),
        game_tree.TileGameTree(C4, [1, 2], [])]), game_tree.TileGameTree(G8, [1, 3], []),
                                            game_tree.TileGameTree(D6, [19, 37], [
                                                game_tree.TileGameTree(D5, [3, 4], [
                                                    game_tree.TileGameTree(C5, [2, 3], [
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(C7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D7, [2, 9], [
                                                    game_tree.TileGameTree(C7, [1, 2], [])]),
                                                game_tree.TileGameTree(C6, [7, 8], [
                                                    game_tree.TileGameTree(H4, [1, 2], []),
                                                    game_tree.TileGameTree(C7, [1, 3], []),
                                                    game_tree.TileGameTree(B6, [2, 3], [
                                                        game_tree.TileGameTree(A6, [1, 2], [])]),
                                                    game_tree.TileGameTree(C5, [1, 2], [])])]),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 3], []),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(H7, [2, 3], []),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(F7, [2, 3], []),
                                            game_tree.TileGameTree(C6, [2, 2], []),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], [])]),
    game_tree.TileGameTree(F6, [180, 732], [game_tree.TileGameTree(G6, [12, 38], [
        game_tree.TileGameTree(G5, [3, 5], [game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], [])]),
        game_tree.TileGameTree(H6, [1, 3], []),
        game_tree.TileGameTree(G7, [2, 5], [game_tree.TileGameTree(H7, [1, 2], [])]),
        game_tree.TileGameTree(A7, [2, 2], [game_tree.TileGameTree(C6, [1, 2], [])])]),
                                            game_tree.TileGameTree(F7, [17, 41], [
                                                game_tree.TileGameTree(F8, [2, 6], [
                                                    game_tree.TileGameTree(G8, [1, 2], [])]),
                                                game_tree.TileGameTree(E7, [2, 7], [
                                                    game_tree.TileGameTree(E8, [1, 2], [])]),
                                                game_tree.TileGameTree(G7, [3, 4], [
                                                    game_tree.TileGameTree(G8, [1, 2], []),
                                                    game_tree.TileGameTree(G6, [2, 2], [
                                                        game_tree.TileGameTree(G5, [1, 2], [])])]),
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(A8, [1, 2], [])]),
                                            game_tree.TileGameTree(E6, [20, 28], [
                                                game_tree.TileGameTree(D6, [6, 7], [
                                                    game_tree.TileGameTree(D5, [2, 3], [
                                                        game_tree.TileGameTree(D4, [1, 2], [])]),
                                                    game_tree.TileGameTree(C6, [3, 3], [
                                                        game_tree.TileGameTree(C5, [1, 2], []),
                                                        game_tree.TileGameTree(B6, [1, 2], [])]),
                                                    game_tree.TileGameTree(H1, [1, 2], [])]),
                                                game_tree.TileGameTree(E7, [3, 8], [
                                                    game_tree.TileGameTree(F7, [2, 2], [
                                                        game_tree.TileGameTree(F8, [1, 2], [])]),
                                                    game_tree.TileGameTree(D7, [2, 2], [
                                                        game_tree.TileGameTree(B7, [1, 2], [])])]),
                                                game_tree.TileGameTree(C8, [1, 2], []),
                                                game_tree.TileGameTree(H1, [1, 2], []),
                                                game_tree.TileGameTree(E5, [1, 4], []),
                                                game_tree.TileGameTree(C6, [2, 2], [
                                                    game_tree.TileGameTree(C7, [1, 2], [])])]),
                                            game_tree.TileGameTree(F5, [23, 37], [
                                                game_tree.TileGameTree(E5, [2, 8], [
                                                    game_tree.TileGameTree(E4, [2, 2], [
                                                        game_tree.TileGameTree(E3, [1, 2], [])])]),
                                                game_tree.TileGameTree(G5, [1, 5], []),
                                                game_tree.TileGameTree(H8, [1, 2], []),
                                                game_tree.TileGameTree(F4, [6, 8], [
                                                    game_tree.TileGameTree(E4, [1, 2], []),
                                                    game_tree.TileGameTree(H2, [1, 2], []),
                                                    game_tree.TileGameTree(F3, [3, 4], [
                                                        game_tree.TileGameTree(G3, [1, 2], []),
                                                        game_tree.TileGameTree(F2, [2, 2], [
                                                            game_tree.TileGameTree(B4, [2, 2], [
                                                                game_tree.TileGameTree(H5, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(D5, [1, 2], []),
                                                game_tree.TileGameTree(G4, [2, 2], [
                                                    game_tree.TileGameTree(H4, [1, 2], [])]),
                                                game_tree.TileGameTree(A2, [1, 2], [])]),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(F4, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(G2, [2, 2], [
                                                game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(D2, [1, 3], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(B2, [1, 2], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(C6, [2, 2], [
                                                game_tree.TileGameTree(B8, [1, 2], [])]),
                                            game_tree.TileGameTree(H7, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(B5, [2, 2], [])]),
    game_tree.TileGameTree(G6, [137, 730], [game_tree.TileGameTree(F6, [14, 28], [
        game_tree.TileGameTree(F5, [1, 4], []), game_tree.TileGameTree(B7, [1, 2], []),
        game_tree.TileGameTree(E4, [1, 2], []), game_tree.TileGameTree(E6, [4, 5], [
            game_tree.TileGameTree(E7, [1, 2], []), game_tree.TileGameTree(G3, [1, 2], []),
            game_tree.TileGameTree(E5, [2, 2], [game_tree.TileGameTree(F5, [1, 2], [])])]),
        game_tree.TileGameTree(C6, [2, 2], [game_tree.TileGameTree(C5, [1, 2], [])]),
        game_tree.TileGameTree(F7, [2, 4], [game_tree.TileGameTree(F8, [1, 2], [])])]),
                                            game_tree.TileGameTree(G7, [11, 26], [
                                                game_tree.TileGameTree(H7, [1, 6], []),
                                                game_tree.TileGameTree(C1, [1, 3], []),
                                                game_tree.TileGameTree(F7, [2, 3], [
                                                    game_tree.TileGameTree(F6, [2, 2], [
                                                        game_tree.TileGameTree(E6, [1, 2], [])])]),
                                                game_tree.TileGameTree(G2, [1, 2], [])]),
                                            game_tree.TileGameTree(G5, [16, 27], [
                                                game_tree.TileGameTree(F7, [1, 2], []),
                                                game_tree.TileGameTree(H5, [1, 5], []),
                                                game_tree.TileGameTree(G4, [5, 5], [
                                                    game_tree.TileGameTree(H4, [1, 2], []),
                                                    game_tree.TileGameTree(G3, [1, 3], []),
                                                    game_tree.TileGameTree(F4, [1, 2], [])]),
                                                game_tree.TileGameTree(F5, [2, 5], [
                                                    game_tree.TileGameTree(F4, [1, 2], [])]),
                                                game_tree.TileGameTree(A5, [1, 2], []),
                                                game_tree.TileGameTree(F1, [2, 2], [])]),
                                            game_tree.TileGameTree(H6, [2, 22], [
                                                game_tree.TileGameTree(F2, [1, 2], [])]),
                                            game_tree.TileGameTree(A2, [2, 3], []),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(D6, [3, 3], [
                                                game_tree.TileGameTree(H5, [2, 2], [])]),
                                            game_tree.TileGameTree(B2, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(D7, [1, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(B5, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], [])]),
    game_tree.TileGameTree(H6, [97, 805], [game_tree.TileGameTree(G6, [3, 33], [
        game_tree.TileGameTree(G5, [2, 2], [
            game_tree.TileGameTree(H5, [2, 2], [game_tree.TileGameTree(D1, [1, 2], [])])]),
        game_tree.TileGameTree(F6, [2, 2], [game_tree.TileGameTree(F7, [1, 2], [])])]),
                                           game_tree.TileGameTree(H7, [8, 17], [
                                               game_tree.TileGameTree(H8, [1, 3], []),
                                               game_tree.TileGameTree(G8, [1, 2], []),
                                               game_tree.TileGameTree(G7, [1, 3], []),
                                               game_tree.TileGameTree(H2, [1, 2], []),
                                               game_tree.TileGameTree(C1, [1, 2], [])]),
                                           game_tree.TileGameTree(H2, [2, 2], [
                                               game_tree.TileGameTree(G1, [1, 2], [])]),
                                           game_tree.TileGameTree(H5, [20, 20], [
                                               game_tree.TileGameTree(H4, [10, 10], [
                                                   game_tree.TileGameTree(H3, [4, 6], [
                                                       game_tree.TileGameTree(H2, [1, 3], []),
                                                       game_tree.TileGameTree(G3, [1, 2], [])]),
                                                   game_tree.TileGameTree(G4, [3, 4], [
                                                       game_tree.TileGameTree(F4, [1, 2], []),
                                                       game_tree.TileGameTree(G3, [2, 2], [
                                                           game_tree.TileGameTree(G2, [1, 2],
                                                                                  [])])]),
                                                   game_tree.TileGameTree(D8, [1, 2], [])]),
                                               game_tree.TileGameTree(G5, [2, 9], [
                                                   game_tree.TileGameTree(F5, [1, 2], [])]),
                                               game_tree.TileGameTree(B8, [1, 2], []),
                                               game_tree.TileGameTree(E1, [1, 2], [])]),
                                           game_tree.TileGameTree(H4, [1, 2], []),
                                           game_tree.TileGameTree(D2, [2, 2], []),
                                           game_tree.TileGameTree(G8, [1, 3], []),
                                           game_tree.TileGameTree(G2, [1, 2], []),
                                           game_tree.TileGameTree(E6, [1, 2], []),
                                           game_tree.TileGameTree(F1, [1, 2], []),
                                           game_tree.TileGameTree(G1, [1, 2], []),
                                           game_tree.TileGameTree(E1, [1, 2], []),
                                           game_tree.TileGameTree(C8, [1, 2], []),
                                           game_tree.TileGameTree(F7, [1, 2], [])]),
    game_tree.TileGameTree(A7, [100, 791], [game_tree.TileGameTree(A6, [15, 24], [
        game_tree.TileGameTree(B6, [2, 6], [
            game_tree.TileGameTree(B7, [2, 2], [game_tree.TileGameTree(B8, [1, 2], [])])]),
        game_tree.TileGameTree(A2, [1, 2], []), game_tree.TileGameTree(D4, [1, 2], []),
        game_tree.TileGameTree(H3, [1, 2], []), game_tree.TileGameTree(A5, [6, 6], [
            game_tree.TileGameTree(A4, [2, 4], [game_tree.TileGameTree(A3, [1, 2], [])]),
            game_tree.TileGameTree(F3, [1, 2], []), game_tree.TileGameTree(B5, [1, 2], [])]),
        game_tree.TileGameTree(H5, [1, 2], [])]), game_tree.TileGameTree(A8, [5, 28], [
        game_tree.TileGameTree(B8, [4, 4], [game_tree.TileGameTree(C8, [3, 3], [
            game_tree.TileGameTree(D8, [2, 3], [
                game_tree.TileGameTree(C4, [2, 2], [game_tree.TileGameTree(C5, [1, 2], [])])])]),
                                            game_tree.TileGameTree(B7, [1, 2], [])]),
        game_tree.TileGameTree(G2, [1, 2], [])]), game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(D7, [2, 2], [
                                                game_tree.TileGameTree(E5, [1, 2], [])]),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(B7, [8, 13], [
                                                game_tree.TileGameTree(H6, [1, 2], []),
                                                game_tree.TileGameTree(B8, [2, 3], [
                                                    game_tree.TileGameTree(C8, [2, 2], [
                                                        game_tree.TileGameTree(D8, [2, 2], [
                                                            game_tree.TileGameTree(E8, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(B6, [1, 3], []),
                                                game_tree.TileGameTree(C7, [3, 3], [
                                                    game_tree.TileGameTree(B8, [1, 2], []),
                                                    game_tree.TileGameTree(C8, [2, 2], [
                                                        game_tree.TileGameTree(D2, [2, 2], [
                                                            game_tree.TileGameTree(C2, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(H5, [1, 3], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(C3, [2, 2], [
                                                game_tree.TileGameTree(D3, [2, 2], [
                                                    game_tree.TileGameTree(E3, [2, 2], [
                                                        game_tree.TileGameTree(E2, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(H8, [2, 3], []),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(H4, [2, 2], [
                                                game_tree.TileGameTree(H3, [1, 2], [])]),
                                            game_tree.TileGameTree(C1, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], [])]),
    game_tree.TileGameTree(B7, [150, 733], [game_tree.TileGameTree(A7, [11, 32], [
        game_tree.TileGameTree(A6, [2, 5], [game_tree.TileGameTree(B1, [1, 2], [])]),
        game_tree.TileGameTree(B3, [1, 2], []), game_tree.TileGameTree(A8, [2, 5], [
            game_tree.TileGameTree(D3, [2, 2], [
                game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(E2, [1, 2], [])])])])]),
                                            game_tree.TileGameTree(C7, [21, 31], [
                                                game_tree.TileGameTree(C8, [4, 9], [
                                                    game_tree.TileGameTree(D8, [2, 3], [
                                                        game_tree.TileGameTree(D7, [2, 2], [
                                                            game_tree.TileGameTree(D6, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(B8, [2, 2], [
                                                        game_tree.TileGameTree(A8, [2, 2], [
                                                            game_tree.TileGameTree(A7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(D7, [9, 9], [
                                                    game_tree.TileGameTree(D8, [1, 4], []),
                                                    game_tree.TileGameTree(D6, [2, 4], [
                                                        game_tree.TileGameTree(D5, [1, 2], [])]),
                                                    game_tree.TileGameTree(E7, [3, 3], [
                                                        game_tree.TileGameTree(E8, [2, 2], [
                                                            game_tree.TileGameTree(F8, [1, 2],
                                                                                   [])]),
                                                        game_tree.TileGameTree(E6, [1, 2], [])])]),
                                                game_tree.TileGameTree(C6, [2, 4], [
                                                    game_tree.TileGameTree(C5, [1, 2], [])]),
                                                game_tree.TileGameTree(A4, [1, 2], [])]),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(B6, [11, 27], [
                                                game_tree.TileGameTree(C6, [3, 4], [
                                                    game_tree.TileGameTree(C5, [2, 2], [
                                                        game_tree.TileGameTree(B5, [2, 2], [
                                                            game_tree.TileGameTree(B4, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C7, [2, 2], [
                                                        game_tree.TileGameTree(C8, [2, 2], [
                                                            game_tree.TileGameTree(B8, [2, 2], [
                                                                game_tree.TileGameTree(A8, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(B5, [3, 3], [
                                                    game_tree.TileGameTree(A5, [1, 2], []),
                                                    game_tree.TileGameTree(B4, [2, 2], [
                                                        game_tree.TileGameTree(C4, [1, 2], [])])]),
                                                game_tree.TileGameTree(A6, [2, 5], [
                                                    game_tree.TileGameTree(A7, [2, 2], [
                                                        game_tree.TileGameTree(A4, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(B8, [1, 23], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(D8, [1, 2], []),
                                            game_tree.TileGameTree(E8, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], []),
                                            game_tree.TileGameTree(G6, [2, 2], []),
                                            game_tree.TileGameTree(B4, [2, 2], [
                                                game_tree.TileGameTree(G7, [1, 2], [])]),
                                            game_tree.TileGameTree(A3, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 3], []),
                                            game_tree.TileGameTree(C6, [2, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(B5, [2, 2], [
                                                game_tree.TileGameTree(C4, [2, 2], [])]),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(F6, [1, 2], []),
                                            game_tree.TileGameTree(E5, [2, 2], [
                                                game_tree.TileGameTree(H5, [1, 2], [])]),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(G5, [1, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], [])]),
    game_tree.TileGameTree(C7, [197, 712], [game_tree.TileGameTree(C8, [5, 33], [
        game_tree.TileGameTree(B8, [1, 3], []), game_tree.TileGameTree(H4, [1, 2], []),
        game_tree.TileGameTree(D8, [2, 2], [game_tree.TileGameTree(E8, [2, 2], [
            game_tree.TileGameTree(E7, [2, 2], [game_tree.TileGameTree(F7, [1, 2], [])])])])]),
                                            game_tree.TileGameTree(D7, [25, 38], [
                                                game_tree.TileGameTree(D8, [3, 9], [
                                                    game_tree.TileGameTree(E8, [2, 3], [
                                                        game_tree.TileGameTree(E7, [2, 2], [
                                                            game_tree.TileGameTree(F7, [2, 2], [
                                                                game_tree.TileGameTree(C1, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(D6, [4, 11], [
                                                    game_tree.TileGameTree(D5, [2, 2], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])]),
                                                    game_tree.TileGameTree(C6, [1, 2], []),
                                                    game_tree.TileGameTree(E6, [1, 2], [])]),
                                                game_tree.TileGameTree(D1, [1, 2], []),
                                                game_tree.TileGameTree(E7, [5, 5], [
                                                    game_tree.TileGameTree(E6, [2, 2], [
                                                        game_tree.TileGameTree(F6, [1, 2], [])]),
                                                    game_tree.TileGameTree(F5, [2, 2], [
                                                        game_tree.TileGameTree(F4, [1, 2], [])]),
                                                    game_tree.TileGameTree(F7, [2, 3], [
                                                        game_tree.TileGameTree(F6, [1, 2], [])])]),
                                                game_tree.TileGameTree(C6, [1, 2], [])]),
                                            game_tree.TileGameTree(B7, [32, 45], [
                                                game_tree.TileGameTree(B6, [3, 13], [
                                                    game_tree.TileGameTree(C6, [2, 2], [
                                                        game_tree.TileGameTree(D6, [1, 2], [])]),
                                                    game_tree.TileGameTree(A6, [1, 2], [])]),
                                                game_tree.TileGameTree(A7, [8, 14], [
                                                    game_tree.TileGameTree(A8, [1, 6], []),
                                                    game_tree.TileGameTree(A6, [2, 3], [
                                                        game_tree.TileGameTree(B6, [2, 2], [
                                                            game_tree.TileGameTree(C6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(B8, [2, 4], [
                                                    game_tree.TileGameTree(C8, [2, 2], [
                                                        game_tree.TileGameTree(A4, [1, 2], [])])]),
                                                game_tree.TileGameTree(A2, [1, 2], []),
                                                game_tree.TileGameTree(F7, [1, 2], []),
                                                game_tree.TileGameTree(G2, [1, 2], [])]),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(C6, [21, 37], [
                                                game_tree.TileGameTree(D6, [4, 8], [
                                                    game_tree.TileGameTree(D7, [1, 2], []),
                                                    game_tree.TileGameTree(D5, [2, 3], [
                                                        game_tree.TileGameTree(C5, [1, 2], [])])]),
                                                game_tree.TileGameTree(B6, [1, 3], []),
                                                game_tree.TileGameTree(C5, [3, 7], [
                                                    game_tree.TileGameTree(D5, [1, 2], []),
                                                    game_tree.TileGameTree(C4, [2, 2], [
                                                        game_tree.TileGameTree(D4, [1, 2], [])])]),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(H7, [1, 2], []),
                                                game_tree.TileGameTree(A7, [1, 2], []),
                                                game_tree.TileGameTree(E2, [2, 2], [
                                                    game_tree.TileGameTree(D2, [2, 2], [
                                                        game_tree.TileGameTree(G3, [1, 2], [])])]),
                                                game_tree.TileGameTree(E3, [1, 2], [])]),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 4], []),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 3], []),
                                            game_tree.TileGameTree(E5, [1, 2], []),
                                            game_tree.TileGameTree(B8, [1, 2], [])]),
    game_tree.TileGameTree(D7, [213, 696], [game_tree.TileGameTree(C7, [28, 38], [
        game_tree.TileGameTree(C8, [3, 8], [game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(D8, [2, 2], [
                                                game_tree.TileGameTree(E7, [1, 2], [])])]),
        game_tree.TileGameTree(B7, [6, 12], [
            game_tree.TileGameTree(A7, [2, 4], [game_tree.TileGameTree(A8, [1, 2], [])]),
            game_tree.TileGameTree(B8, [1, 3], [])]), game_tree.TileGameTree(C6, [1, 6], []),
        game_tree.TileGameTree(D4, [1, 2], []), game_tree.TileGameTree(E5, [1, 2], []),
        game_tree.TileGameTree(F1, [1, 2], []), game_tree.TileGameTree(B1, [1, 2], [])]),
                                            game_tree.TileGameTree(E7, [30, 44], [
                                                game_tree.TileGameTree(E6, [2, 10], [
                                                    game_tree.TileGameTree(F6, [1, 2], [])]),
                                                game_tree.TileGameTree(E8, [1, 8], []),
                                                game_tree.TileGameTree(F7, [9, 11], [
                                                    game_tree.TileGameTree(F8, [1, 4], []),
                                                    game_tree.TileGameTree(G7, [4, 4], [
                                                        game_tree.TileGameTree(G8, [1, 2], []),
                                                        game_tree.TileGameTree(G6, [1, 3], [])]),
                                                    game_tree.TileGameTree(B3, [1, 2], []),
                                                    game_tree.TileGameTree(F6, [1, 2], [])]),
                                                game_tree.TileGameTree(G4, [1, 2], []),
                                                game_tree.TileGameTree(B6, [1, 2], []),
                                                game_tree.TileGameTree(A5, [2, 2], [])]),
                                            game_tree.TileGameTree(D6, [17, 36], [
                                                game_tree.TileGameTree(B2, [1, 2], []),
                                                game_tree.TileGameTree(D5, [9, 11], [
                                                    game_tree.TileGameTree(E5, [1, 5], []),
                                                    game_tree.TileGameTree(D4, [3, 4], [
                                                        game_tree.TileGameTree(C4, [1, 2], []),
                                                        game_tree.TileGameTree(E4, [2, 2], [
                                                            game_tree.TileGameTree(E3, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(C5, [2, 2], [
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(B6, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(E5, [1, 2], []),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(E2, [2, 2], []),
                                                game_tree.TileGameTree(E6, [1, 3], [])]),
                                            game_tree.TileGameTree(F8, [1, 2], []),
                                            game_tree.TileGameTree(D3, [2, 2], [
                                                game_tree.TileGameTree(D2, [2, 2], [
                                                    game_tree.TileGameTree(G8, [1, 2], [])])]),
                                            game_tree.TileGameTree(D8, [6, 36], [
                                                game_tree.TileGameTree(E8, [3, 3], [
                                                    game_tree.TileGameTree(F8, [3, 3], [
                                                        game_tree.TileGameTree(A6, [1, 2], []),
                                                        game_tree.TileGameTree(F7, [1, 2], [])])]),
                                                game_tree.TileGameTree(C8, [2, 3], [
                                                    game_tree.TileGameTree(C7, [1, 2], [])]),
                                                game_tree.TileGameTree(D5, [1, 2], [])]),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(H7, [2, 3], [
                                                game_tree.TileGameTree(F6, [1, 2], [])]),
                                            game_tree.TileGameTree(B4, [1, 2], []),
                                            game_tree.TileGameTree(B2, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(H1, [2, 2], []),
                                            game_tree.TileGameTree(E8, [2, 3], [
                                                game_tree.TileGameTree(F8, [1, 2], [])]),
                                            game_tree.TileGameTree(H4, [2, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(A8, [1, 2], []),
                                            game_tree.TileGameTree(G4, [1, 2], []),
                                            game_tree.TileGameTree(G1, [1, 2], []),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], [])]),
    game_tree.TileGameTree(E7, [176, 674], [game_tree.TileGameTree(E6, [14, 31], [
        game_tree.TileGameTree(E5, [5, 9], [game_tree.TileGameTree(D5, [2, 3], [
            game_tree.TileGameTree(D6, [2, 2], [game_tree.TileGameTree(G2, [1, 2], [])])]),
                                            game_tree.TileGameTree(E4, [2, 3], [
                                                game_tree.TileGameTree(E3, [2, 2], [
                                                    game_tree.TileGameTree(E2, [1, 2], [])])])]),
        game_tree.TileGameTree(B2, [1, 2], []), game_tree.TileGameTree(G6, [1, 2], []),
        game_tree.TileGameTree(F6, [2, 2], [game_tree.TileGameTree(G6, [1, 2], [])]),
        game_tree.TileGameTree(D6, [2, 2], [game_tree.TileGameTree(D5, [1, 2], [])]),
        game_tree.TileGameTree(B7, [1, 2], [])]), game_tree.TileGameTree(F7, [27, 38], [
        game_tree.TileGameTree(F8, [3, 11], [
            game_tree.TileGameTree(E8, [3, 3], [game_tree.TileGameTree(D8, [1, 3], [])])]),
        game_tree.TileGameTree(G7, [8, 9], [game_tree.TileGameTree(H7, [1, 3], []),
                                            game_tree.TileGameTree(G6, [2, 3], [
                                                game_tree.TileGameTree(G5, [2, 2], [
                                                    game_tree.TileGameTree(G4, [2, 2], [
                                                        game_tree.TileGameTree(F4, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(G8, [2, 4], [
                                                game_tree.TileGameTree(F8, [2, 2], [
                                                    game_tree.TileGameTree(E8, [1, 2], [])])])]),
        game_tree.TileGameTree(E1, [1, 2], []), game_tree.TileGameTree(H6, [1, 2], []),
        game_tree.TileGameTree(F6, [2, 4], [game_tree.TileGameTree(F5, [2, 2], [
            game_tree.TileGameTree(F4, [2, 2], [game_tree.TileGameTree(G4, [1, 2], [])])])]),
        game_tree.TileGameTree(B3, [1, 2], []), game_tree.TileGameTree(H3, [1, 2], []),
        game_tree.TileGameTree(E2, [1, 2], [])]), game_tree.TileGameTree(E8, [7, 41], [
        game_tree.TileGameTree(D8, [4, 4], [game_tree.TileGameTree(C8, [3, 3], [
            game_tree.TileGameTree(C7, [2, 2], [game_tree.TileGameTree(B7, [1, 2], [])]),
            game_tree.TileGameTree(B8, [2, 2], [game_tree.TileGameTree(A8, [1, 2], [])])]),
                                            game_tree.TileGameTree(D7, [2, 2], [
                                                game_tree.TileGameTree(D6, [1, 2], [])])]),
        game_tree.TileGameTree(F8, [2, 4], [game_tree.TileGameTree(G8, [1, 2], [])])]),
                                            game_tree.TileGameTree(D7, [10, 20], [
                                                game_tree.TileGameTree(D8, [2, 7], [
                                                    game_tree.TileGameTree(E8, [2, 2], [
                                                        game_tree.TileGameTree(F8, [2, 2], [
                                                            game_tree.TileGameTree(G8, [2, 2], [
                                                                game_tree.TileGameTree(H8, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(C7, [3, 3], [
                                                    game_tree.TileGameTree(B7, [1, 2], []),
                                                    game_tree.TileGameTree(C6, [1, 2], [])]),
                                                game_tree.TileGameTree(D6, [1, 2], [])]),
                                            game_tree.TileGameTree(H6, [1, 3], []),
                                            game_tree.TileGameTree(B8, [1, 3], []),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(D4, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(B1, [2, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(H2, [2, 2], []),
                                            game_tree.TileGameTree(D2, [2, 2], [
                                                game_tree.TileGameTree(D1, [1, 2], [])]),
                                            game_tree.TileGameTree(G8, [2, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(F5, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(E3, [2, 2], [
                                                game_tree.TileGameTree(F3, [1, 2], [])])]),
    game_tree.TileGameTree(F7, [151, 735], [game_tree.TileGameTree(G3, [2, 2], [
        game_tree.TileGameTree(G4, [2, 2], [game_tree.TileGameTree(H4, [1, 2], [])])]),
                                            game_tree.TileGameTree(C8, [1, 2], []),
                                            game_tree.TileGameTree(E7, [17, 27], [
                                                game_tree.TileGameTree(D7, [5, 8], [
                                                    game_tree.TileGameTree(C7, [1, 2], []),
                                                    game_tree.TileGameTree(D6, [1, 3], []),
                                                    game_tree.TileGameTree(D8, [2, 2], [
                                                        game_tree.TileGameTree(E8, [2, 2], [
                                                            game_tree.TileGameTree(G1, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(F6, [1, 2], []),
                                                game_tree.TileGameTree(E6, [3, 4], [
                                                    game_tree.TileGameTree(E5, [2, 2], [
                                                        game_tree.TileGameTree(A3, [1, 2], [])]),
                                                    game_tree.TileGameTree(A4, [1, 2], [])]),
                                                game_tree.TileGameTree(E8, [1, 5], []),
                                                game_tree.TileGameTree(H6, [1, 2], [])]),
                                            game_tree.TileGameTree(G7, [11, 29], [
                                                game_tree.TileGameTree(G8, [1, 6], []),
                                                game_tree.TileGameTree(H7, [1, 4], []),
                                                game_tree.TileGameTree(G6, [2, 3], [
                                                    game_tree.TileGameTree(G5, [2, 2], [
                                                        game_tree.TileGameTree(H5, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(F6, [13, 33], [
                                                game_tree.TileGameTree(F5, [3, 5], [
                                                    game_tree.TileGameTree(F4, [2, 3], [
                                                        game_tree.TileGameTree(F3, [2, 2], [
                                                            game_tree.TileGameTree(F2, [2, 2], [
                                                                game_tree.TileGameTree(F1, [2, 2], [
                                                                    game_tree.TileGameTree(G1,
                                                                                           [1, 2],
                                                                                           [])])])])])]),
                                                game_tree.TileGameTree(E5, [1, 2], []),
                                                game_tree.TileGameTree(G6, [2, 6], [
                                                    game_tree.TileGameTree(G7, [1, 2], [])]),
                                                game_tree.TileGameTree(E6, [2, 3], [
                                                    game_tree.TileGameTree(D6, [2, 2], [
                                                        game_tree.TileGameTree(C6, [2, 2], [
                                                            game_tree.TileGameTree(C7, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(F8, [4, 24], [
                                                game_tree.TileGameTree(G8, [3, 4], [
                                                    game_tree.TileGameTree(G7, [1, 2], []),
                                                    game_tree.TileGameTree(H8, [1, 2], [])])]),
                                            game_tree.TileGameTree(C3, [1, 2], []),
                                            game_tree.TileGameTree(D7, [2, 2], [
                                                game_tree.TileGameTree(C2, [2, 2], [])]),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 3], []),
                                            game_tree.TileGameTree(A6, [1, 3], []),
                                            game_tree.TileGameTree(C2, [1, 2], []),
                                            game_tree.TileGameTree(E1, [1, 2], []),
                                            game_tree.TileGameTree(C5, [2, 2], []),
                                            game_tree.TileGameTree(B8, [2, 2], []),
                                            game_tree.TileGameTree(B6, [1, 2], []),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], [])]),
    game_tree.TileGameTree(G7, [109, 784], [
        game_tree.TileGameTree(G8, [2, 20], [game_tree.TileGameTree(H8, [1, 2], [])]),
        game_tree.TileGameTree(G6, [9, 12], [game_tree.TileGameTree(F6, [1, 3], []),
                                             game_tree.TileGameTree(H6, [1, 3], []),
                                             game_tree.TileGameTree(G5, [4, 5], [
                                                 game_tree.TileGameTree(F5, [2, 3], [
                                                     game_tree.TileGameTree(E5, [2, 2], [
                                                         game_tree.TileGameTree(E4, [2, 2], [
                                                             game_tree.TileGameTree(E3, [2, 2], [
                                                                 game_tree.TileGameTree(E2, [2, 2],
                                                                                        [
                                                                                            game_tree.TileGameTree(
                                                                                                E1,
                                                                                                [1,
                                                                                                 2],
                                                                                                [])])])])])]),
                                                 game_tree.TileGameTree(D1, [1, 2], [])])]),
        game_tree.TileGameTree(H7, [2, 21], [game_tree.TileGameTree(H8, [1, 2], [])]),
        game_tree.TileGameTree(F7, [14, 20], [game_tree.TileGameTree(F8, [3, 8], [
            game_tree.TileGameTree(G8, [1, 2], []), game_tree.TileGameTree(H7, [1, 2], [])]),
                                              game_tree.TileGameTree(E7, [3, 4], [
                                                  game_tree.TileGameTree(D7, [2, 3], [
                                                      game_tree.TileGameTree(D6, [2, 2], [
                                                          game_tree.TileGameTree(E6, [2, 2], [
                                                              game_tree.TileGameTree(E5, [1, 2],
                                                                                     [])])])])]),
                                              game_tree.TileGameTree(F6, [2, 3], [
                                                  game_tree.TileGameTree(F5, [2, 2], [
                                                      game_tree.TileGameTree(F4, [2, 2], [
                                                          game_tree.TileGameTree(G4, [1, 2],
                                                                                 [])])])]),
                                              game_tree.TileGameTree(C5, [1, 2], [])]),
        game_tree.TileGameTree(B2, [1, 3], []),
        game_tree.TileGameTree(E2, [2, 3], [game_tree.TileGameTree(F2, [1, 2], [])]),
        game_tree.TileGameTree(F2, [3, 3], [game_tree.TileGameTree(E2, [2, 2], [
            game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(D1, [1, 2], [])])])]),
        game_tree.TileGameTree(G2, [2, 2], [game_tree.TileGameTree(E6, [1, 2], [])]),
        game_tree.TileGameTree(A7, [1, 2], []), game_tree.TileGameTree(C1, [2, 3], [
            game_tree.TileGameTree(A5, [2, 2], [game_tree.TileGameTree(G2, [1, 2], [])])]),
        game_tree.TileGameTree(F1, [1, 2], []), game_tree.TileGameTree(B4, [1, 2], []),
        game_tree.TileGameTree(C6, [1, 2], []), game_tree.TileGameTree(A2, [1, 2], []),
        game_tree.TileGameTree(A4, [2, 2], []), game_tree.TileGameTree(G4, [1, 2], []),
        game_tree.TileGameTree(A5, [1, 2], []), game_tree.TileGameTree(A8, [1, 2], []),
        game_tree.TileGameTree(E7, [2, 2], [game_tree.TileGameTree(G2, [1, 2], [])]),
        game_tree.TileGameTree(G5, [2, 2], [game_tree.TileGameTree(F2, [1, 2], [])]),
        game_tree.TileGameTree(C8, [1, 2], [])]), game_tree.TileGameTree(H7, [61, 839], [
        game_tree.TileGameTree(H6, [15, 15], [game_tree.TileGameTree(E4, [1, 2], []),
                                              game_tree.TileGameTree(E8, [1, 2], []),
                                              game_tree.TileGameTree(H5, [8, 9], [
                                                  game_tree.TileGameTree(H4, [4, 7], [
                                                      game_tree.TileGameTree(G4, [1, 3], []),
                                                      game_tree.TileGameTree(C8, [2, 2], [
                                                          game_tree.TileGameTree(B8, [2, 2], [
                                                              game_tree.TileGameTree(E8, [1, 2],
                                                                                     [])])])]),
                                                  game_tree.TileGameTree(G5, [1, 2], [])]),
                                              game_tree.TileGameTree(G6, [1, 3], []),
                                              game_tree.TileGameTree(D7, [1, 2], []),
                                              game_tree.TileGameTree(C6, [1, 2], [])]),
        game_tree.TileGameTree(H8, [1, 15], []), game_tree.TileGameTree(G7, [1, 16], []),
        game_tree.TileGameTree(D7, [1, 2], []), game_tree.TileGameTree(C1, [1, 2], []),
        game_tree.TileGameTree(C3, [1, 3], []), game_tree.TileGameTree(B2, [1, 2], []),
        game_tree.TileGameTree(A7, [1, 2], []), game_tree.TileGameTree(D3, [1, 3], []),
        game_tree.TileGameTree(B6, [1, 2], []), game_tree.TileGameTree(E1, [1, 2], []),
        game_tree.TileGameTree(A6, [2, 2], [game_tree.TileGameTree(E1, [1, 2], [])])]),
    game_tree.TileGameTree(A8, [46, 794], [game_tree.TileGameTree(B8, [18, 18], [
        game_tree.TileGameTree(C8, [8, 9], [
            game_tree.TileGameTree(C7, [2, 5], [game_tree.TileGameTree(C6, [1, 2], [])]),
            game_tree.TileGameTree(D8, [3, 4], [game_tree.TileGameTree(E8, [2, 2], [
                game_tree.TileGameTree(D2, [2, 2], [game_tree.TileGameTree(D3, [1, 2], [])])]),
                                                game_tree.TileGameTree(D7, [1, 2], [])])]),
        game_tree.TileGameTree(B7, [1, 5], []), game_tree.TileGameTree(G2, [1, 2], []),
        game_tree.TileGameTree(D1, [1, 2], []), game_tree.TileGameTree(F7, [1, 3], []),
        game_tree.TileGameTree(E1, [1, 2], [])]), game_tree.TileGameTree(G6, [1, 2], []),
                                           game_tree.TileGameTree(A7, [2, 16], [
                                               game_tree.TileGameTree(B7, [1, 2], [])]),
                                           game_tree.TileGameTree(H6, [2, 2], []),
                                           game_tree.TileGameTree(F4, [1, 2], []),
                                           game_tree.TileGameTree(H4, [1, 2], []),
                                           game_tree.TileGameTree(B3, [2, 2], [
                                               game_tree.TileGameTree(H7, [2, 2], [])]),
                                           game_tree.TileGameTree(A1, [2, 2], []),
                                           game_tree.TileGameTree(D7, [1, 2], []),
                                           game_tree.TileGameTree(F8, [1, 2], [])]),
    game_tree.TileGameTree(B8, [98, 785], [game_tree.TileGameTree(A8, [17, 31], [
        game_tree.TileGameTree(A7, [2, 9], [
            game_tree.TileGameTree(B7, [2, 2], [game_tree.TileGameTree(B6, [1, 2], [])])]),
        game_tree.TileGameTree(C6, [2, 2], [game_tree.TileGameTree(B6, [2, 2], [
            game_tree.TileGameTree(A6, [2, 2], [game_tree.TileGameTree(F7, [1, 2], [])])])]),
        game_tree.TileGameTree(A5, [1, 3], []), game_tree.TileGameTree(B1, [1, 2], []),
        game_tree.TileGameTree(G2, [2, 3], [game_tree.TileGameTree(G1, [1, 2], [])]),
        game_tree.TileGameTree(B5, [1, 2], []), game_tree.TileGameTree(H7, [1, 2], [])]),
                                           game_tree.TileGameTree(C8, [19, 21], [
                                               game_tree.TileGameTree(C7, [4, 12], [
                                                   game_tree.TileGameTree(B7, [1, 2], []),
                                                   game_tree.TileGameTree(D7, [2, 3], [
                                                       game_tree.TileGameTree(D6, [1, 2], [])])]),
                                               game_tree.TileGameTree(D1, [2, 2], [
                                                   game_tree.TileGameTree(E6, [1, 2], [])]),
                                               game_tree.TileGameTree(D8, [4, 6], [
                                                   game_tree.TileGameTree(D7, [1, 3], []),
                                                   game_tree.TileGameTree(E8, [2, 2], [
                                                       game_tree.TileGameTree(F8, [2, 2], [
                                                           game_tree.TileGameTree(F7, [1, 2],
                                                                                  [])])])]),
                                               game_tree.TileGameTree(E4, [1, 2], [])]),
                                           game_tree.TileGameTree(B7, [5, 23], [
                                               game_tree.TileGameTree(A7, [1, 4], []),
                                               game_tree.TileGameTree(C7, [1, 2], [])]),
                                           game_tree.TileGameTree(H5, [2, 2], []),
                                           game_tree.TileGameTree(C1, [2, 4], []),
                                           game_tree.TileGameTree(B1, [1, 2], []),
                                           game_tree.TileGameTree(A3, [1, 2], []),
                                           game_tree.TileGameTree(B6, [1, 2], []),
                                           game_tree.TileGameTree(B2, [1, 3], []),
                                           game_tree.TileGameTree(C4, [1, 2], []),
                                           game_tree.TileGameTree(H1, [1, 2], []),
                                           game_tree.TileGameTree(F3, [2, 2], [
                                               game_tree.TileGameTree(C1, [1, 2], [])])]),
    game_tree.TileGameTree(C8, [151, 745], [game_tree.TileGameTree(B8, [31, 43], [
        game_tree.TileGameTree(A8, [9, 19], [
            game_tree.TileGameTree(A7, [2, 8], [game_tree.TileGameTree(B7, [1, 2], [])]),
            game_tree.TileGameTree(B5, [1, 2], [])]),
        game_tree.TileGameTree(B7, [2, 8], [game_tree.TileGameTree(C7, [1, 2], [])]),
        game_tree.TileGameTree(B6, [2, 2], [game_tree.TileGameTree(B5, [2, 2], [
            game_tree.TileGameTree(G4, [2, 2], [game_tree.TileGameTree(H2, [1, 2], [])])])]),
        game_tree.TileGameTree(E6, [1, 2], []), game_tree.TileGameTree(B3, [1, 2], []),
        game_tree.TileGameTree(E7, [2, 2], [game_tree.TileGameTree(G5, [1, 2], [])]),
        game_tree.TileGameTree(A7, [1, 2], [])]), game_tree.TileGameTree(D8, [36, 44], [
        game_tree.TileGameTree(D7, [3, 15], [game_tree.TileGameTree(D6, [1, 3], [])]),
        game_tree.TileGameTree(E8, [14, 18], [game_tree.TileGameTree(D1, [1, 2], []),
                                              game_tree.TileGameTree(F8, [2, 6], [
                                                  game_tree.TileGameTree(G8, [1, 2], [])]),
                                              game_tree.TileGameTree(E7, [2, 6], [
                                                  game_tree.TileGameTree(E6, [2, 2], [
                                                      game_tree.TileGameTree(E5, [2, 2], [
                                                          game_tree.TileGameTree(E4, [1, 2],
                                                                                 [])])])]),
                                              game_tree.TileGameTree(E2, [1, 2], []),
                                              game_tree.TileGameTree(A8, [1, 2], [])]),
        game_tree.TileGameTree(E5, [1, 2], []), game_tree.TileGameTree(H3, [2, 2], [
            game_tree.TileGameTree(H2, [2, 2], [
                game_tree.TileGameTree(H1, [2, 2], [game_tree.TileGameTree(H5, [1, 2], [])])])]),
        game_tree.TileGameTree(A8, [1, 2], []), game_tree.TileGameTree(C2, [1, 2], [])]),
                                            game_tree.TileGameTree(C7, [5, 27], [
                                                game_tree.TileGameTree(B7, [2, 3], [
                                                    game_tree.TileGameTree(B8, [2, 2], [
                                                        game_tree.TileGameTree(A8, [2, 2], [
                                                            game_tree.TileGameTree(A7, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(C6, [3, 3], [
                                                    game_tree.TileGameTree(B6, [1, 3], [])])]),
                                            game_tree.TileGameTree(C6, [1, 2], []),
                                            game_tree.TileGameTree(H3, [1, 2], []),
                                            game_tree.TileGameTree(D2, [1, 2], []),
                                            game_tree.TileGameTree(B1, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(F2, [2, 2], [
                                                game_tree.TileGameTree(E2, [2, 2], [
                                                    game_tree.TileGameTree(A3, [2, 2], [
                                                        game_tree.TileGameTree(A4, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(A6, [1, 2], []),
                                            game_tree.TileGameTree(F3, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(D6, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(H6, [1, 2], []),
                                            game_tree.TileGameTree(E2, [1, 2], [])]),
    game_tree.TileGameTree(D8, [174, 747], [game_tree.TileGameTree(E8, [29, 39], [
        game_tree.TileGameTree(A4, [1, 2], []), game_tree.TileGameTree(F8, [11, 16], [
            game_tree.TileGameTree(F7, [2, 5], [game_tree.TileGameTree(E7, [1, 2], [])]),
            game_tree.TileGameTree(G4, [1, 2], []), game_tree.TileGameTree(G8, [4, 5], [
                game_tree.TileGameTree(G7, [1, 2], []), game_tree.TileGameTree(H8, [1, 3], [])]),
            game_tree.TileGameTree(B6, [1, 2], [])]), game_tree.TileGameTree(E7, [5, 8], [
            game_tree.TileGameTree(F7, [1, 2], []),
            game_tree.TileGameTree(D7, [2, 3], [game_tree.TileGameTree(C7, [1, 2], [])]),
            game_tree.TileGameTree(E6, [1, 2], [])]), game_tree.TileGameTree(B1, [1, 2], []),
        game_tree.TileGameTree(H1, [1, 2], []), game_tree.TileGameTree(G4, [1, 2], []),
        game_tree.TileGameTree(C2, [1, 2], []), game_tree.TileGameTree(H2, [2, 2], [
            game_tree.TileGameTree(H1, [2, 2], [game_tree.TileGameTree(G1, [1, 2], [])])])]),
                                            game_tree.TileGameTree(D7, [6, 38], [
                                                game_tree.TileGameTree(E7, [3, 3], [
                                                    game_tree.TileGameTree(F7, [2, 2], [
                                                        game_tree.TileGameTree(B8, [2, 2], [
                                                            game_tree.TileGameTree(A8, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E6, [1, 2], [])]),
                                                game_tree.TileGameTree(D6, [1, 3], []),
                                                game_tree.TileGameTree(C7, [2, 2], [
                                                    game_tree.TileGameTree(B7, [1, 2], [])])]),
                                            game_tree.TileGameTree(C8, [39, 51], [
                                                game_tree.TileGameTree(B8, [10, 14], [
                                                    game_tree.TileGameTree(A8, [3, 3], [
                                                        game_tree.TileGameTree(C3, [1, 2], []),
                                                        game_tree.TileGameTree(A7, [1, 2], [])]),
                                                    game_tree.TileGameTree(B7, [1, 6], []),
                                                    game_tree.TileGameTree(H3, [1, 2], []),
                                                    game_tree.TileGameTree(G6, [2, 2], [
                                                        game_tree.TileGameTree(F6, [1, 2], [])])]),
                                                game_tree.TileGameTree(C7, [8, 22], [
                                                    game_tree.TileGameTree(C6, [1, 2], []),
                                                    game_tree.TileGameTree(D7, [3, 5], [
                                                        game_tree.TileGameTree(E7, [2, 3], [
                                                            game_tree.TileGameTree(E8, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(B7, [3, 3], [
                                                        game_tree.TileGameTree(B6, [1, 2], []),
                                                        game_tree.TileGameTree(A7, [1, 2], [])])]),
                                                game_tree.TileGameTree(B5, [1, 2], []),
                                                game_tree.TileGameTree(B3, [1, 2], []),
                                                game_tree.TileGameTree(F1, [1, 2], []),
                                                game_tree.TileGameTree(D2, [1, 2], [])]),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(H4, [1, 2], []),
                                            game_tree.TileGameTree(B8, [2, 2], [
                                                game_tree.TileGameTree(A8, [2, 2], [
                                                    game_tree.TileGameTree(A7, [1, 2], [])])]),
                                            game_tree.TileGameTree(D3, [1, 2], []),
                                            game_tree.TileGameTree(B4, [2, 2], [
                                                game_tree.TileGameTree(F7, [2, 2], [])]),
                                            game_tree.TileGameTree(F6, [2, 3], [
                                                game_tree.TileGameTree(G6, [1, 2], [])]),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(G3, [1, 2], []),
                                            game_tree.TileGameTree(C2, [2, 2], [
                                                game_tree.TileGameTree(C1, [1, 2], [])]),
                                            game_tree.TileGameTree(E4, [1, 2], []),
                                            game_tree.TileGameTree(C3, [1, 2], []),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(H7, [1, 3], []),
                                            game_tree.TileGameTree(E7, [1, 2], []),
                                            game_tree.TileGameTree(F1, [1, 2], []),
                                            game_tree.TileGameTree(C7, [1, 2], []),
                                            game_tree.TileGameTree(F7, [1, 2], []),
                                            game_tree.TileGameTree(G7, [1, 2], [])]),
    game_tree.TileGameTree(E8, [162, 753], [game_tree.TileGameTree(E7, [5, 35], [
        game_tree.TileGameTree(D7, [2, 2], [
            game_tree.TileGameTree(D8, [2, 2], [game_tree.TileGameTree(C8, [1, 2], [])])]),
        game_tree.TileGameTree(F7, [2, 3], [game_tree.TileGameTree(G6, [1, 2], [])]),
        game_tree.TileGameTree(E6, [2, 2], [game_tree.TileGameTree(F6, [1, 2], [])])]),
                                            game_tree.TileGameTree(F8, [29, 45], [
                                                game_tree.TileGameTree(F7, [3, 12], [
                                                    game_tree.TileGameTree(E7, [2, 2], [
                                                        game_tree.TileGameTree(D7, [2, 2], [
                                                            game_tree.TileGameTree(D6, [2, 2], [
                                                                game_tree.TileGameTree(D5, [1, 2],
                                                                                       [])])])]),
                                                    game_tree.TileGameTree(F6, [2, 2], [
                                                        game_tree.TileGameTree(F5, [2, 2], [
                                                            game_tree.TileGameTree(G5, [1, 2],
                                                                                   [])])])]),
                                                game_tree.TileGameTree(B1, [1, 2], []),
                                                game_tree.TileGameTree(G5, [1, 2], []),
                                                game_tree.TileGameTree(G8, [13, 14], [
                                                    game_tree.TileGameTree(D6, [1, 2], []),
                                                    game_tree.TileGameTree(H8, [1, 7], []),
                                                    game_tree.TileGameTree(G7, [1, 5], []),
                                                    game_tree.TileGameTree(D3, [1, 2], [])]),
                                                game_tree.TileGameTree(H2, [1, 2], []),
                                                game_tree.TileGameTree(B2, [2, 2], [
                                                    game_tree.TileGameTree(A2, [1, 2], [])])]),
                                            game_tree.TileGameTree(G8, [1, 2], []),
                                            game_tree.TileGameTree(D8, [34, 40], [
                                                game_tree.TileGameTree(C8, [14, 17], [
                                                    game_tree.TileGameTree(C7, [2, 6], [
                                                        game_tree.TileGameTree(C6, [1, 2], [])]),
                                                    game_tree.TileGameTree(B8, [4, 8], [
                                                        game_tree.TileGameTree(B7, [1, 2], []),
                                                        game_tree.TileGameTree(A8, [1, 3], [])]),
                                                    game_tree.TileGameTree(E5, [1, 2], [])]),
                                                game_tree.TileGameTree(D7, [5, 12], [
                                                    game_tree.TileGameTree(E7, [2, 2], [
                                                        game_tree.TileGameTree(E6, [1, 2], [])]),
                                                    game_tree.TileGameTree(D6, [1, 2], []),
                                                    game_tree.TileGameTree(C7, [2, 3], [
                                                        game_tree.TileGameTree(C8, [2, 2], [
                                                            game_tree.TileGameTree(B8, [2, 2], [
                                                                game_tree.TileGameTree(A8, [1, 2],
                                                                                       [])])])])]),
                                                game_tree.TileGameTree(C6, [1, 2], []),
                                                game_tree.TileGameTree(A6, [2, 2], [
                                                    game_tree.TileGameTree(C2, [1, 2], [])]),
                                                game_tree.TileGameTree(G2, [2, 2], [
                                                    game_tree.TileGameTree(G3, [2, 2], [
                                                        game_tree.TileGameTree(H3, [1, 2], [])])]),
                                                game_tree.TileGameTree(A4, [1, 2], []),
                                                game_tree.TileGameTree(F5, [1, 2], []),
                                                game_tree.TileGameTree(G5, [1, 2], [])]),
                                            game_tree.TileGameTree(B8, [2, 2], [
                                                game_tree.TileGameTree(H7, [1, 2], [])]),
                                            game_tree.TileGameTree(B7, [1, 2], []),
                                            game_tree.TileGameTree(D3, [1, 3], []),
                                            game_tree.TileGameTree(G6, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(A5, [2, 2], [
                                                game_tree.TileGameTree(A4, [2, 2], [
                                                    game_tree.TileGameTree(B4, [1, 2], [])])]),
                                            game_tree.TileGameTree(A7, [1, 2], []),
                                            game_tree.TileGameTree(A2, [1, 2], []),
                                            game_tree.TileGameTree(E3, [1, 2], []),
                                            game_tree.TileGameTree(D5, [1, 2], []),
                                            game_tree.TileGameTree(D6, [2, 2], []),
                                            game_tree.TileGameTree(A4, [1, 2], []),
                                            game_tree.TileGameTree(A1, [1, 2], []),
                                            game_tree.TileGameTree(G2, [1, 2], []),
                                            game_tree.TileGameTree(A6, [2, 2], []),
                                            game_tree.TileGameTree(D1, [1, 2], []),
                                            game_tree.TileGameTree(G1, [2, 2], [
                                                game_tree.TileGameTree(G2, [2, 2], [
                                                    game_tree.TileGameTree(C8, [2, 2], [
                                                        game_tree.TileGameTree(C7, [1, 2],
                                                                               [])])])])]),
    game_tree.TileGameTree(F8, [108, 772], [game_tree.TileGameTree(G8, [13, 24], [
        game_tree.TileGameTree(H8, [1, 3], []), game_tree.TileGameTree(G7, [1, 8], []),
        game_tree.TileGameTree(F3, [1, 2], []), game_tree.TileGameTree(D2, [1, 2], []),
        game_tree.TileGameTree(H2, [1, 2], [])]), game_tree.TileGameTree(E8, [27, 28], [
        game_tree.TileGameTree(D8, [11, 16], [game_tree.TileGameTree(D7, [2, 3], [
            game_tree.TileGameTree(C7, [2, 2], [
                game_tree.TileGameTree(C8, [2, 2], [game_tree.TileGameTree(B8, [1, 2], [])])])]),
                                              game_tree.TileGameTree(B7, [1, 2], []),
                                              game_tree.TileGameTree(C8, [5, 5], [
                                                  game_tree.TileGameTree(G2, [1, 2], []),
                                                  game_tree.TileGameTree(B8, [3, 3], [
                                                      game_tree.TileGameTree(D5, [1, 2], []),
                                                      game_tree.TileGameTree(A8, [2, 2], [
                                                          game_tree.TileGameTree(A7, [1, 2],
                                                                                 [])])]),
                                                  game_tree.TileGameTree(C7, [1, 2], [])]),
                                              game_tree.TileGameTree(E2, [1, 2], []),
                                              game_tree.TileGameTree(D6, [2, 2], [
                                                  game_tree.TileGameTree(E6, [2, 2], [
                                                      game_tree.TileGameTree(E5, [1, 2], [])])]),
                                              game_tree.TileGameTree(A7, [1, 2], [])]),
        game_tree.TileGameTree(D4, [1, 2], []), game_tree.TileGameTree(E7, [3, 8], [
            game_tree.TileGameTree(E6, [1, 2], []), game_tree.TileGameTree(F7, [1, 2], [])]),
        game_tree.TileGameTree(A3, [2, 2], [game_tree.TileGameTree(B3, [1, 2], [])]),
        game_tree.TileGameTree(D5, [2, 2], [game_tree.TileGameTree(C5, [1, 2], [])]),
        game_tree.TileGameTree(C1, [2, 2], [game_tree.TileGameTree(D1, [2, 2], [
            game_tree.TileGameTree(E1, [2, 2], [game_tree.TileGameTree(F1, [1, 2], [])])])])]),
                                            game_tree.TileGameTree(B6, [2, 3], [
                                                game_tree.TileGameTree(C6, [1, 2], [])]),
                                            game_tree.TileGameTree(H5, [1, 2], []),
                                            game_tree.TileGameTree(F7, [5, 26], [
                                                game_tree.TileGameTree(G7, [2, 3], [
                                                    game_tree.TileGameTree(H7, [1, 2], [])]),
                                                game_tree.TileGameTree(E7, [3, 3], [
                                                    game_tree.TileGameTree(D7, [2, 2], [
                                                        game_tree.TileGameTree(C7, [2, 2], [
                                                            game_tree.TileGameTree(C8, [1, 2],
                                                                                   [])])]),
                                                    game_tree.TileGameTree(E8, [2, 2], [
                                                        game_tree.TileGameTree(F2, [2, 2], [
                                                            game_tree.TileGameTree(E2, [1, 2],
                                                                                   [])])])])]),
                                            game_tree.TileGameTree(B8, [1, 2], []),
                                            game_tree.TileGameTree(H8, [1, 2], []),
                                            game_tree.TileGameTree(A5, [1, 2], []),
                                            game_tree.TileGameTree(E6, [1, 2], []),
                                            game_tree.TileGameTree(H2, [1, 2], []),
                                            game_tree.TileGameTree(A4, [2, 3], []),
                                            game_tree.TileGameTree(B1, [1, 3], []),
                                            game_tree.TileGameTree(B3, [1, 2], []),
                                            game_tree.TileGameTree(H1, [1, 2], []),
                                            game_tree.TileGameTree(G7, [1, 2], [])]),
    game_tree.TileGameTree(G8, [68, 830], [game_tree.TileGameTree(F8, [20, 20], [
        game_tree.TileGameTree(E8, [9, 9], [game_tree.TileGameTree(D8, [4, 4], [
            game_tree.TileGameTree(H3, [1, 2], []), game_tree.TileGameTree(D7, [1, 3], [])]),
                                            game_tree.TileGameTree(E7, [3, 4], [
                                                game_tree.TileGameTree(E6, [1, 2], []),
                                                game_tree.TileGameTree(D7, [2, 2], [
                                                    game_tree.TileGameTree(C7, [2, 2], [
                                                        game_tree.TileGameTree(C8, [1, 2],
                                                                               [])])])]),
                                            game_tree.TileGameTree(H6, [2, 2], [
                                                game_tree.TileGameTree(H7, [2, 2], [
                                                    game_tree.TileGameTree(G7, [1, 2], [])])]),
                                            game_tree.TileGameTree(E3, [1, 2], [])]),
        game_tree.TileGameTree(F7, [4, 9], [game_tree.TileGameTree(G7, [1, 2], []),
                                            game_tree.TileGameTree(E7, [2, 2], [
                                                game_tree.TileGameTree(E6, [1, 2], [])]),
                                            game_tree.TileGameTree(H5, [1, 2], [])]),
        game_tree.TileGameTree(G1, [1, 2], []), game_tree.TileGameTree(B7, [2, 2], []),
        game_tree.TileGameTree(A5, [1, 2], [])]), game_tree.TileGameTree(H8, [1, 12], []),
                                           game_tree.TileGameTree(G1, [1, 2], []),
                                           game_tree.TileGameTree(G7, [2, 18], [
                                               game_tree.TileGameTree(F7, [2, 2], [
                                                   game_tree.TileGameTree(F8, [2, 2], [
                                                       game_tree.TileGameTree(E8, [2, 2], [
                                                           game_tree.TileGameTree(E7, [2, 2], [
                                                               game_tree.TileGameTree(C3, [1, 2],
                                                                                      [])])])])])]),
                                           game_tree.TileGameTree(A8, [1, 2], []),
                                           game_tree.TileGameTree(A7, [1, 2], []),
                                           game_tree.TileGameTree(F7, [1, 2], []),
                                           game_tree.TileGameTree(F4, [1, 2], []),
                                           game_tree.TileGameTree(B5, [1, 2], []),
                                           game_tree.TileGameTree(B6, [1, 2], []),
                                           game_tree.TileGameTree(B3, [1, 2], []),
                                           game_tree.TileGameTree(C3, [1, 2], []),
                                           game_tree.TileGameTree(A4, [1, 2], []),
                                           game_tree.TileGameTree(E7, [1, 2], [])]),
    game_tree.TileGameTree(H8, [1, 793], []), game_tree.TileGameTree(A1, [27, 201], []),
    game_tree.TileGameTree(B1, [36, 201], []), game_tree.TileGameTree(C1, [49, 201], []),
    game_tree.TileGameTree(D1, [54, 201], []), game_tree.TileGameTree(E1, [47, 201], []),
    game_tree.TileGameTree(F1, [39, 201], []), game_tree.TileGameTree(G1, [38, 201], []),
    game_tree.TileGameTree(H1, [28, 201], []), game_tree.TileGameTree(A2, [49, 201], []),
    game_tree.TileGameTree(B2, [59, 201], []), game_tree.TileGameTree(C2, [69, 201], []),
    game_tree.TileGameTree(D2, [72, 201], []), game_tree.TileGameTree(E2, [75, 201], []),
    game_tree.TileGameTree(F2, [62, 201], []), game_tree.TileGameTree(G2, [59, 201], []),
    game_tree.TileGameTree(H2, [40, 201], []), game_tree.TileGameTree(A3, [57, 201], []),
    game_tree.TileGameTree(B3, [58, 201], []), game_tree.TileGameTree(C3, [65, 201], []),
    game_tree.TileGameTree(D3, [65, 201], []), game_tree.TileGameTree(E3, [71, 200], []),
    game_tree.TileGameTree(F3, [64, 200], []), game_tree.TileGameTree(G3, [69, 201], []),
    game_tree.TileGameTree(H3, [50, 201], []), game_tree.TileGameTree(A4, [60, 201], []),
    game_tree.TileGameTree(B4, [66, 201], []), game_tree.TileGameTree(C4, [79, 201], []),
    game_tree.TileGameTree(D4, [78, 201], []), game_tree.TileGameTree(E4, [72, 200], []),
    game_tree.TileGameTree(F4, [75, 201], []), game_tree.TileGameTree(G4, [67, 201], []),
    game_tree.TileGameTree(H4, [55, 201], []), game_tree.TileGameTree(A5, [62, 201], []),
    game_tree.TileGameTree(B5, [64, 201], []), game_tree.TileGameTree(C5, [71, 201], []),
    game_tree.TileGameTree(D5, [62, 201], []), game_tree.TileGameTree(E5, [59, 201], []),
    game_tree.TileGameTree(F5, [57, 201], []), game_tree.TileGameTree(G5, [58, 201], []),
    game_tree.TileGameTree(H5, [55, 201], []), game_tree.TileGameTree(A6, [47, 201], []),
    game_tree.TileGameTree(B6, [55, 201], []), game_tree.TileGameTree(C6, [73, 201], []),
    game_tree.TileGameTree(D6, [65, 201], []), game_tree.TileGameTree(E6, [60, 200], []),
    game_tree.TileGameTree(F6, [65, 201], []), game_tree.TileGameTree(G6, [57, 200], []),
    game_tree.TileGameTree(H6, [32, 201], []), game_tree.TileGameTree(A7, [32, 201], []),
    game_tree.TileGameTree(B7, [42, 201], []), game_tree.TileGameTree(C7, [61, 201], []),
    game_tree.TileGameTree(D7, [65, 201], []), game_tree.TileGameTree(E7, [61, 201], []),
    game_tree.TileGameTree(F7, [46, 201], []), game_tree.TileGameTree(G7, [40, 200], []),
    game_tree.TileGameTree(H7, [16, 192], []), game_tree.TileGameTree(A8, [25, 201], []),
    game_tree.TileGameTree(B8, [48, 201], []), game_tree.TileGameTree(C8, [62, 201], []),
    game_tree.TileGameTree(D8, [60, 201], []), game_tree.TileGameTree(E8, [51, 201], []),
    game_tree.TileGameTree(F8, [30, 193], []), game_tree.TileGameTree(G8, [20, 200], []),
    game_tree.TileGameTree(H8, [1, 25], [])]))
