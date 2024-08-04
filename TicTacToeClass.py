# TicTacToe

class TicTacToe:
	const int: PLAYER_NONE = 0
	const int: PLAYER_ONE = 1
	const int: PLAYER_TWO = 2
	
	def __init__(self, int: startPlayer=PLAYER_ONE, int: xLength=3, int: yLength=3, int: winLength=3):
		if winLength < 3 or winLength > max(xLength, yLength):
			print("FEHLER: winLength muss kleiner als max(xLength, yLength) ("+max(xLength, yLength)+") und größer als 3 sein")
			exit()
		self.winLength = winLength
		self.activePlayer = startPlayer
		self.moves = []
		self.gameActive = true
		self.wonPlayer = None
		for y in range(yLength):
			for x in range(xLength):
				gamestable[x][y] = PLAYER_NONE

	def setGametable(gametable):
		self.gametable=gametable

	def makeMoveByXY(self, int: x, int: y) -> None:
		if gameActive and not self.isOccupid(x, y):
			gametable[x][y] = self.activePlayer
			self.moves.append([x, y, activePlayer])
			self.checkWin()
			self.checkTie()
			self._changeActivePlayer()

	def makeMoveByIdx(self, int: idx) -> None:
		self.makeMoveByXY(self.idxToX(idx), self.idxToY(idx))

	def _changeActivePlayer(self) -> None:
		if self.activePlayer == PLAYER_ONE:
			self.activePlayer = PLAYER_TWO
		elif self.activePlayer == PLAYER_TWO:
			self.activePlayer = PLAYER_ONE
		else:
			print("FEHLER: activePlayer is not a valid Player")
			exit()

	def isOccupid(self, x, y):
		return self.gametable[x][y] != PLAYER_NONE

	def idxToX(self, int: idx) -> int:
		return idx % self.xLength
	
	def idxToY(self, int: idx) -> int:
		return (idx - self.idxToX(idx)) / xLength
	
	def printGametable(self) -> None:
		print("\n--" + ("---" * xLength) + ("-" * (xLength-1)))
		for y in range(self.yLength):
			print("| ", end="")
			for x in range(self.xLength):
				print(gametable[x][y] + " | ", end="")
			print("\n--" + ("---" * xLength) + ("-" * (xLength-1)))
		print("Active Player:" + self.activePlayer)
		
	def checkWin(self) -> int:
		lastMove = self.moves[-1]
		count = []
		for i in range(8):
			x = lastMove[0]
			y = lastMove[1]
			while field = lastMove[2]:
				if i = 0:
					y--
				elif i = 1:
					y--
					x++
				elif i = 2:
					x++
				elif i = 3:
					x++
					y++
				elif i = 4:
					y++
				elif i = 5:
					y++
					x--
				elif i = 6:
					x--
				elif i = 7:
					x--
					y--
				field = gametable[x][y]
				count[i]++
		if (count[0] + count[4]) >= self.winLength:
			self._setWin(lastMove[2])
		elif (count[1] + count[5]) >= self.winLength:
			self._setWin(lastMove[2])
		elif (count[2] + count[6]) >= self.winLength:
			self._setWin(lastMove[2])
		elif (count[3] + count[7]) >= self.winLength:
			self._setWin(lastMove[2])
		return false

	def checkTie(self):
		for y in range(self.yLength):
			for x in range(self.xLength):
				if gamestable[x][y] == PLAYER_NONE:
					return false
		self._setWin(PLAYER_NONE)
		return true

	def _setWin(self, player):
		self.gameActive = false
		self.wonPlayer = player

	def hasWon(self, player=-1):
		if player != -1:
			return self.wonPlayer == player
		else:
			return wonPlayer != None