import os
from itertools import permutations

art_logo = """
 _____ _        _____             _____           
/__   (_) ___  /__   \__ _  ___  /__   \___   ___
  / /\/ |/ __|   / /\/ _` |/ __|   / /\/ _ \ / __|
 / /  | | (__   / / | (_| | (__   / / | (_) |  __/
 \/   |_|\___|  \/   \__,_|\___|  \/   \___/ \___|
                                                                                                   
"""

win_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
game_is_over = False


def tictactoe():
    print(art_logo)
    # total_moves = 0

    def print_board():
        for i in board:
            print(f' {i[0]} | {i[1]} | {i[2]} ')
            print(f' ------------ ')

    def update_board(player, player_move):
        for row_id, row in enumerate(board):
            for col_id, col in enumerate(row):
                if col == str(player_move):
                    board[row_id][col_id] = str(player)
        print_board()

    def check_score(player, player_moves):
        global game_is_over
        for pos_win in win_pos:
            if all(x in player_moves for x in pos_win):
                print(f"GAME OVER! Player {player} wins the game.")
                game_is_over = True

    players = {"X": [], "O": []}
    print_board()
    player1 = str(input("Select a player. Type X or O to select the player. ")).upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    for move in range(9):
        if move % 2 == 0:
            players_turn = player1
        else:
            players_turn = player2

        player_move = int(input(f"Player {players_turn} - Your turn. Type a number from the board: "))
        players[players_turn].append(player_move)
        update_board(players_turn, player_move)
        check_score(players_turn, players[players_turn])
        if game_is_over:
            return

    print("This is a Draw!")


continue_play = input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n': ")

if continue_play == 'y':
    os.system('clear')
    tictactoe()
