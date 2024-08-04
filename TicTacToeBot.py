from TicTacToeClass import *
class TicTacToeBot:
	def __init__(self, TicTacToe ttt, botsPlayerId):
		self.ttt = ttt
		self.id = botsPlayerId
	def clacBestMove(self, gametable):
		moves = []
		for elmt in self.getPossibleMoves(gametable)
			newGametable = self.ttt.copy()
			newGametable.makeMove(elmt[0], elmt[1])
			if newGametable.hasWon():
				if newGametable.wonPlayer == self.id:
					return elmt
				elif newGametable.wonPlayer == TicTacToe.PLAYER_NONE:
					moves.append([0, elmt])
				else:
					moves.append([-1, elmt])
			else:
				tmp = self._treeFunction(newGametable)
				tmp = tmp[0] / tmp[1]
				moves.append([tmp, elmt])
		tmp = [-2, [0,0]]
		for i in moves:
			if tmp[1] < i[1]:
				tmp = i
		return tmp[1]
			
				
	def _getPossibleMoves(self, gametable):
		possibleMoves = []
		for y in range(self.ttt.yLength):
			for x in range(self.ttt.xLength):
				if gametable[x][y] = TicTacToe.PLAYER_NONE:
					possibleMoves.append([x, y])
		return possibleMoves

	def _treeFunction(self, gametable, j):
		for elmt in self.getPossibleMoves(gametable)
			i = 0
			newGametable = gametable.copy()
			newGametable.makeMove(elmt[0], elmt[1])
			if newGametable.hasWon():
				if newGametable.wonPlayer == self.id:
					i += 1
					j++
				elif newGametable.wonPlayer == TicTacToe.PLAYER_NONE:
					i += 0
					j++
				else:
					i += -1
					j++
			else:
				tmp = self._treeFunction(newGametable, j)
				i += tmp[0]
				j = tmp[1]
		return [i, j]
		