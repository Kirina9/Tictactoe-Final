# Sherol salarzon
# 2020/1/1
# This is a tic tac toe game where players can choose weather if they want to play a two player game or one player game
# When player wants to play with themselfs choose (bot)
# When player wants to play with friends (up to 2 people) choose pc. It will be randomize who will go first, so there
# no advantage for people.
import random
from os import system, name
# X = player1
# O = Player2
# ===================================================
# This is the layout for the board
Board = ['_','_','_',
         "_","_","_",
         '_','_','_']
# ===================================================
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def pc():
    # turns is responsible for randomizing who goes first
    turn = random.randrange(0, 2)
    turn = int(turn)
    #tries is how much slots in the board had left if the 0 turns into 9 it is a tie (it is part of Win condition function)
    tries = 0
    # this function is for player wanted to play with friends(2 players only)
    def main(L):
        while True:
            # Main is where the "Obvservation" happens, this dermine if the player has won or not or a tie, and also this function
            # does all the work for switching turns
            # L is the turn meaning every time the game check the win condition after they add a 1 to turn
            if turn == 0:
                print('================================')
                print('player 1:')
                Player1(L)
                L += 1
                win_condition(L)
                print('=================================')
                print('player 2:')
                Player2(L)
                L += 1
                win_condition(L)
                print('=================================')
                print(L)

            elif turn == 1:
                print('================================')
                print('player 2:')
                Player2(L)
                L += 1
                win_condition(L)
                print('=================================')
                print('player 1:')
                Player1(L)
                L += 1
                win_condition(L)
                print('=================================')
                print(L)

    def Player1(L):
        # This is where player 1's takes to choose where he wants to go.
        place = input('1-9: ')
        place = int(place) - 1
        clear()
        # determine if the player 1 placed somewhere that has already been taken or not. It also determine if the player
        # enter higher number then the maximum or minimum
        if place > 8:
            print('You have passed the limit')
            print('it is your turn again player 1')
            Player1(L)
        elif place < 0:
            print('you have less than the minimum')
            print('it is your turn again player 1')
            Player1(L)
        else:
            if Board[place] == 'O':
                print('Player two has already put something there')
                Player1(L)
            elif Board[place] == 'X':
                print('You have already put something there')
                Player1(L)
            else:
                Board[place] = 'X'
                show(L)

    def Player2(L):
        # This is where player 2's takes to choose where he wants to go.
        place = input('1-9: ')
        place = int(place) - 1
        clear()
        # determine if the player 2 placed somewhere that has already been taken or not. It also determine if the player
        # enter higher number then the maximum or minimum
        if place > 8:
            print('You have passed the limit')
            print('your turn again player 2')
            Player2(L)
        elif place < 0:
            print('you have less than the minimum')
            print('your turn again player 2')
            Player2(L)
        else:
            if Board[place] == 'X':
                print('Player One has already put something there')
                Player2(L)
            else:
                Board[place] = 'O'
                show(L)
    def show(L):
        # This show the board after they placed after they position it
        print(Board[0],"|",Board[1],"|",Board[2])
        print(Board[3],"|",Board[4],"|",Board[5])
        print(Board[6],"|",Board[7],"|",Board[8])
        L += 1
    main(tries)
def vsbots():
    # This is for player wanted to play by himself
    # rand is for randomly choosing who goes first
    # 0 is Player
    # 1 is Bots
    rand = random.randrange(0,2)
    rand = int(rand)
    bots = random.randrange(9)
    turn = 9
    print(rand)
    while turn >= 0:
        def mainer():
            # same as the other side this determine the win condition and turns
            if rand == 0:
                print('player goes first')
                player()
                win_condition()
                bots()
                win_condition()
            elif rand == 1:
                print('Bots goes first')
                bots()
                win_condition()
                player()
                win_condition()

        def player():
            # same one the other side this is for the player to choose.
            while True:
                place = input('1-9: ')
                try:
                    place = int(place) - 1
                    if place > 8:
                        print('You have passed the limit')
                    else:
                        if Board[place] == 'O':
                            print('Player two has already put something there')
                            player()
                        elif Board[place] == 'X':
                            print('You have already put something there')
                            player()
                        else:
                            Board[place] = 'X'
                            print('========================')
                            show()
                            print('========================')
                            break
                except ValueError:
                    print('LMAO')

        def bots():
            # this is for the bots, it randomly chooses from 1 - 9 on the board
            boots = random.randrange(0,9) - 1
            if Board[boots] == 'X':
                print('Player two has already put something there')
                bots()
            elif Board[boots] == 'O':
                print('You have already put something there')
                bots()
            else:
                Board[boots] = 'O'
                print('========================')
                show()
                print('========================')

        def show():
            print(Board[0], "|", Board[1], "|", Board[2])
            print(Board[3], "|", Board[4], "|", Board[5])
            print(Board[6], "|", Board[7], "|", Board[8])
        mainer()


def win_condition(L):
    if Board[0] == 'X' and Board[1] == 'X' and Board[2] == 'X' or Board[0] == 'O' and Board[1] == 'O' and Board[2] == 'O':
        if Board[0] == 'X' and Board[1] == 'X' and Board[2] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[0] == 'O' and Board[1] == 'O' and Board[2] == 'O':
            print('player 2 wins')
            exit()
    elif Board[3] == 'X' and Board[4] == 'X' and Board[5] == 'X' or Board[3] == 'O' and Board[4] == 'O' and Board[5] == 'O':
        if Board[3] == 'X' and Board[4] == 'X' and Board[5] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[3] == 'O' and Board[4] == 'O' and Board[5] == 'O':
            print('player 2 wins')
            exit()
    elif Board[6] == 'X' and Board[7] == 'X' and Board[8] == 'X' or Board[6] == 'O' and Board[7] == 'O' and Board[8] == 'O':
        if Board[6] == 'X' and Board[7] == 'X' and Board[8] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[6] == 'O' and Board[7] == 'O' and Board[8] == 'O':
            print('player 2 wins')
            exit()
    elif Board[0] == 'X' and Board[3] == 'X' and Board[6] == 'X' or Board[0] == 'O' and Board[3] == 'O' and Board[6] == 'O':
        if Board[0] == 'X' and Board[3] == 'X' and Board[6] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[0] == 'O' and Board[3] == 'O' and Board[6] == 'O':
            print('player 2 wins')
            exit()
    elif Board[1] == 'X' and Board[4] == 'X' and Board[7] == 'X' or Board[1] == 'O' and Board[4] == 'O' and Board[7] == 'O':
        if Board[1] == 'X' and Board[4] == 'X' and Board[7] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[1] == 'O' and Board[4] == 'O' and Board[7] == 'O':
            print('player 2 wins')
            exit()
    elif Board[2] == 'X' and Board[5] == 'X' and Board[8] == 'X' or Board[2] == 'O' and Board[5] == 'O' and Board[8] == 'O':
        if Board[2] == 'X' and Board[5] == 'X' and Board[8] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[2] == 'O' and Board[5] == 'O' and Board[8] == 'O':
            print('player 2 wins')
            exit()
    elif Board[0] == 'X' and Board[4] == 'X' and Board[8] == 'X' or Board[0] == 'O' and Board[4] == 'O' and Board[8] == 'O':
        if Board[0] == 'X' and Board[4] == 'X' and Board[8] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[0] == 'O' and Board[4] == 'O' and Board[8] == 'O':
            print('player 2 wins')
            exit()
    elif Board[2] == 'X' and Board[4] == 'X' and Board[6] == 'X' or Board[2] == 'O' and Board[4] == 'O' and Board[6] == 'O':
        if Board[2] == 'X' and Board[4] == 'X' and Board[6] == 'X':
            print('Player 1 wins')
            exit()
        elif Board[2] == 'X' and Board[4] == 'X' and Board[6] == 'O':
            print('player 2 wins')
            exit()
    elif L == 9:
        print('its a tie')
        exit()
# user chooses if 1 player or 2 players.
print('pc = 2 players')
print('bot = 1 player')
Choose = input('pc or bot: ')
Choose = str.lower(Choose)
tries = 9
if Choose == 'pc':
    print('This is a 2 player game')
    print('here is the layout of the board')
    print('1','|','2','|','3')
    print('4','|','5','|','6')
    print('7','|','8','|','9')
    pc()
else:
    print('here is the layout of the board')
    print('1','|','2','|','3')
    print('4','|','5','|','6')
    print('7','|','8','|','9')
    vsbots()