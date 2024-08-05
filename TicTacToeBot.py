from TicTacToeClass import *
import copy

class TicTacToeBot:
    def __init__(self, game, bot_player_id):
        # Initialisiert den Bot mit dem TicTacToe-Spiel und der Spieler-ID des Bots
        self.game = game
        self.bot_player_id = bot_player_id

    def calculate_best_move(self, game_board):
        # Berechnet den besten Zug basierend auf dem aktuellen Spielbrett
        best_score = float('-inf')
        best_move = None
        for move in self._get_possible_moves(game_board):
            self.game.setGametable(copy.deepcopy(game_board))
            self.game.makeMoveByXY(move[0], move[1])
            score = self._minimax(self.game.gametable, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def _get_possible_moves(self, game_board):
        # Gibt eine Liste aller möglichen Züge zurück, die auf dem aktuellen Spielbrett gemacht werden können
        possible_moves = []
        for y in range(self.game.yLength):
            for x in range(self.game.xLength):
                if game_board[x][y] == Player.NONE:
                    possible_moves.append([x, y])
        return possible_moves

    def _minimax(self, game_board, is_maximizing):
        # Implementiert den Minimax-Algorithmus, um den besten Zug zu finden
        if self.game.hasWon(Player.ONE):
            return -10  # Verlust für den Bot
        elif self.game.hasWon(Player.TWO):
            return 10   # Gewinn für den Bot
        elif self.game.checkTie():
            return 0    # Unentschieden
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self._get_possible_moves(game_board):
                self.game.setGametable(copy.deepcopy(game_board))
                self.game.makeMoveByXY(move[0], move[1])
                score = self._minimax(self.game.gametable, False)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self._get_possible_moves(game_board):
                self.game.setGametable(copy.deepcopy(game_board))
                self.game.makeMoveByXY(move[0], move[1])
                score = self._minimax(self.game.gametable, True)
                best_score = min(score, best_score)
            return best_score
