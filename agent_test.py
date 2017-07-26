"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


def timeleft():
    return 1000

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def timeleft():
        return 1000

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        self.player2 = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        self.game = isolation.Board(self.player1, self.player2)

    def test_basic(self):
        """just testing the testing"""
        print("Starting my unit test\n")
        self.game.apply_move( (3,3) ) # simple first move for player 1
        print(self.game.to_string())
        self.game.apply_move( (3,4) ) # simple first move for player 2
        print(self.game.to_string())
        msg = ''
        while msg != 'Q':
            nextgo = self.player1.get_move(self.game, lambda: 1000)
            if nextgo == (-1,-1):
                print("Player 1 lost")
                return
            print("Player 1", nextgo)
            self.game.apply_move(nextgo)
            print(self.game.to_string())
            nextgo = self.player2.get_move(self.game, lambda: 1000)
            if nextgo == (-1,-1):
                print("Player 2 lost")
                return
            print("Player 2", nextgo)
            self.game.apply_move(nextgo)
            print(self.game.to_string())
           # msg = input(">")


if __name__ == '__main__':
    unittest.main()
