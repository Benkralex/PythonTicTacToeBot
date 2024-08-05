from TicTacToeClass import *
from TicTacToeBot import *
import copy

ttt = TicTacToe(startPlayer=Player.ONE)
bot = TicTacToeBot(copy.deepcopy(ttt), Player.TWO)
ttt.printGametable()

while ttt.gameActive:
    if ttt.activePlayer == Player.ONE:
        try:
            move = int(input("Make a move: "))
            ttt.makeMoveByIdx(move)
        except ValueError:
            print("Invalid input. Please enter a valid move.")
    elif ttt.activePlayer == Player.TWO:
        move = bot.calculate_best_move(copy.deepcopy(ttt.gametable))
        print(move)
        ttt.makeMoveByXY(move[0], move[1])
    else:
        print("FEHLER: activePlayer is not a valid Player")
        exit()
    ttt.printGametable()

print("Game Over")
print("Player " + str(ttt.wonPlayer) + " has won!") if ttt.wonPlayer != Player.NONE else print("It's a tie!")
