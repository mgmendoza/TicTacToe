import random

WINNING_COMBOS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

game_on = True

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

rule_board = ("1", "2", "3",
              "4", "5", "6",
              "7", "8", "9")


def table():
    print("---------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")


x = []
o = []


def player_1():
    table()
    space = int(input("Player 1. Choose your square from 1-9: ")) - 1
    if space < 0 or space >= 9:
        print("Invalid choice. Try again.")
        player_1()
    elif board[space] == " ":
        board[space] = 'x'
        x.append(space + 1)
    else:
        print('Square not valid. Please choose again.')
        player_1()


def player_2():
    table()
    space = int(input("Player 2. Choose your square from 1-9: ")) - 1
    if space < 0 or space >= 9:
        print("Invalid choice. Try again.")
        player_2()
    if board[space] == " ":
        board[space] = 'o'
        o.append(space + 1)
    else:
        print('Square not valid. Please choose again.')
        player_2()


def computer_play():
    space = random.randint(1, 9) - 1
    if board[space] == " ":
        board[space] = 'o'
        o.append(space+1)
    else:
        computer_play()


def player1_check():
    for combos in WINNING_COMBOS:
        result = all(space in x for space in combos)
        if result:
            table()
            print('Player 1 wins!')
            return True


def player2_check():
    global game_on
    for combos in WINNING_COMBOS:
        result = all(space in o for space in combos)
        if result:
            table()
            print('Player 2 wins!')
            game_on = False


def computer_check():
    global game_on
    for combos in WINNING_COMBOS:
        result = all(space in o for space in combos)
        if result:
            table()
            print('Computer wins!')
            game_on = False


players = int(input('Welcome to tic-tic-toe! How many players? 1 or 2? '))
if players == 2:
    while game_on:
        player_1()
        if player1_check():
            game_on = False
            break
        turns_count = board.count(" ")
        if turns_count < 1:
            table()
            print("it's a tie! Game over.")
            game_on=False
            break
        player_2()
        player2_check()
        turns_count = board.count(" ")
        if turns_count < 1:
            table()
            print("it's a tie! Game over.")
            game_on = False
            break

elif players == 1:
    while game_on:
        player_1()
        if player1_check():
            game_on = False
            break
        turns_count = board.count(" ")
        if turns_count < 1:
            table()
            print("it's a tie! Game over.")
            game_on = False
            break
        computer_play()
        computer_check()
        turns_count = board.count(" ")
        if turns_count < 1:
            table()
            print("it's a tie! Game over.")
            game_on = False
            break