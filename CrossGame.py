'''
* @Author: Uthsavi KP
* @Date: 2020-12-27 18:51:58
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-12-27 18:51:58
* @Title: To play a Cross Game or Tic-Tac-Toe Game. Player 1 is Computer and Player 2 is the user.Player 1 take Random Cell i.e column or row. 

'''

#Initializing And Printing The Empty Board
board = [" "for x in range(1,10)]
def printBoard(board):
    print("-------")
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("-------")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("-------")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")
    print("-------")
printBoard(board) 

#Player 1 is the Computer and the Player 2 is the user.
def playerLetter():
    player=''
    computer=''
    while (player != 'X' and player != 'O'):    #While loop to validate user input
        player=input("User Choose X or O: ").upper()
        print("Player Letter Is: ", player)
        if player == 'X':
            computer = 'O'
        elif player == 'O':
            computer = 'X'
        else:
            print("Invalid Input, Enter Only X or O")
playerLetter()       