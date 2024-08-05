from enum import Enum

# TicTacToe

class TicTacToe:
	PLAYER_NONE = 0;
	PLAYER_ONE = 1;
	PLAYER_TWO = 2;
	
	def __init__(self, startPlayer, xLength=3, yLength=3, winLength=3):
		if winLength < 3 or winLength > max(xLength, yLength):
			print("FEHLER: winLength muss kleiner als max(xLength, yLength) ("+max(xLength, yLength)+") und größer als 3 sein")
			exit()
		self.winLength = winLength
		self.activePlayer = startPlayer
		self.moves = []
		self.gameActive = True
		self.wonPlayer = None
		self.xLength = xLength
		self.yLength = yLength
		self.gametable = [[Player.NONE for y in range(yLength)] for x in range(xLength)]

	def setGametable(self, gametable):
		self.gametable=gametable

	def makeMoveByXY(self, x, y) -> None:
		if self.gameActive and not self.isOccupid(x, y):
			self.gametable[x][y] = self.activePlayer
			self.moves.append([x, y, self.activePlayer])
			self.checkWin()
			self.checkTie()
			self._changeActivePlayer()

	def makeMoveByIdx(self, idx) -> None:
		self.makeMoveByXY(self.idxToX(idx), self.idxToY(idx))

	def _changeActivePlayer(self) -> None:
		if self.activePlayer == Player.ONE:
			self.activePlayer = Player.TWO
		elif self.activePlayer == Player.TWO:
			self.activePlayer = Player.ONE
		else:
			print("FEHLER: activePlayer is not a valid Player")
			exit()

	def isOccupid(self, x, y):
		return self.gametable[x][y] != Player.NONE

	def idxToX(self, idx):
		return idx % self.xLength
	
	def idxToY(self, idx):
		return int(idx / self.xLength)
	
	def printGametable(self):
		print("\n--" + ("---" * self.xLength) + ("-" * (self.xLength-1)))
		for y in range(self.yLength):
			print("| ", end="")
			for x in range(self.xLength):
				if self.gametable[x][y] == Player.ONE:
					player = "1"
				elif self.gametable[x][y] == Player.TWO:
					player = "2"
				else:
					player = " "
				print(player + " | ", end="")
			print("\n--" + ("---" * self.xLength) + ("-" * (self.xLength-1)))
		if self.activePlayer == Player.ONE:
			player = "1"
		elif self.activePlayer == Player.TWO:
			player = "2"
		else:
			player = " "
		print("Active Player:" + player)
		
	def checkWin(self):
		lastMove = self.moves[-1]  # Get the last move made
		count = [0, 0, 0, 0, 0, 0, 0, 0]  # Initialize a count array to keep track of consecutive fields
		directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]  # Define the 8 possible directions
		for i, (dx, dy) in enumerate(directions):  # Iterate through the 8 possible directions
			x, y = lastMove[0], lastMove[1]  # Get the x and y coordinates of the last move
			field = lastMove[2]  # Get the player who made the last move
			while field == lastMove[2]:  # Continue checking in the same direction until a different player is encountered
				x += dx  # Update the x-coordinate based on the direction
				y += dy  # Update the y-coordinate based on the direction
				try:
					field = self.gametable[x][y]  # Get the player at the current position
					if field == lastMove[2]:
						count[i] += 1  # Increment the count for the current direction
				except IndexError:
					break
		if any(c >= self.winLength - 1 for c in (count[0] + count[4], count[1] + count[5], count[2] + count[6], count[3] + count[7])):
			# Check if any of the counts for vertical, diagonal (\), horizontal, or diagonal (/) directions are greater than or equal to the win length
			self._setWin(lastMove[2])  # Set the winning player
		return False  # Return False to indicate that no player has won yet

	def checkTie(self):
		for y in range(self.yLength):
			for x in range(self.xLength):
				if self.gametable[x][y] == Player.NONE:
					return False
		self._setWin(Player.NONE)
		return True

	def _setWin(self, player):
		self.gameActive = False
		self.wonPlayer = player

	def hasWon(self, player=-1):
		if player != -1:
			return self.wonPlayer == player
		else:
			return self.wonPlayer != None
		
class Player(Enum):
	NONE = 0
	ONE = 1
	TWO = 2