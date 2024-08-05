import unittest
from TicTacToeClass import Player, TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_checkWin(self):
        game = TicTacToe(Player.ONE)
        game.board = [[Player.ONE, Player.TWO, Player.ONE],
                      [Player.TWO, Player.ONE, Player.TWO],
                      [Player.ONE, Player.TWO, Player.ONE]]
        self.assertTrue(game.checkWin(Player.ONE))
        self.assertFalse(game.checkWin(Player.TWO))

    def test_checkWin_PlayerOne(self):
        game = TicTacToe(Player.ONE)
        game.board = [[Player.ONE, Player.TWO, Player.ONE],
                      [Player.TWO, Player.ONE, Player.TWO],
                      [Player.ONE, Player.TWO, Player.ONE]]
        self.assertTrue(game.checkWin(Player.ONE))
        self.assertFalse(game.checkWin(Player.TWO))

    def test_checkWin_PlayerTwo(self):
        game = TicTacToe(Player.ONE)
        game.board = [[Player.ONE, Player.TWO, Player.ONE],
                      [Player.TWO, Player.ONE, Player.TWO],
                      [Player.ONE, Player.TWO, Player.ONE]]
        self.assertFalse(game.checkWin(Player.ONE))
        self.assertTrue(game.checkWin(Player.TWO))

if __name__ == '__main__':
    unittest.main()