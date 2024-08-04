from TicTacToeClass import *
from TicTacToeBot import *

ttt = TicTacToe()
bot = TicTacToeBot(ttt, TicTacToe.PLAYER_TWO)

while ttt.active:
	ttt.printGametable()
	if ttt.activePlayer == TicTacToe.PLAYER_ONE:
		ttt.makeMove(input("Zug:"))
	elif ttt.activePlayer == TicTacToe.PLAYER_TWO:
		bot.calcBestMove(ttt.gametable)