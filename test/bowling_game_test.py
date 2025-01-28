import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))
import unittest
from lib.bowling_game import BowlingGame

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_multiple(self, times, pins):
        for _ in range(times):
            self.game.roll(pins)

    def test_gutter_game(self):
        print("- Testing Gutter Game (all rolls 0)...")
        self.roll_multiple(20, 0)
        self.assertEqual(0, self.game.score(), "ERROR: Gutter Game should have a score of 0")
        print("DONE: Gutter Game passed with score 0.\n")

    def test_all_ones(self):
        print("- Testing game with all rolls as 1...")
        self.roll_multiple(20, 1)
        self.assertEqual(20, self.game.score(), "ERROR: Game with all rolls as 1 should have a score of 20")
        print("DONE: Game with all rolls as 1 passed with score 20.\n")

    def test_perfect_game(self):
        print("- Testing Perfect Game (12 strikes)...")
        self.roll_multiple(12, 10)
        self.assertEqual(300, self.game.score(), "ERROR: Perfect Game should have a score of 300")
        print("DONE: Perfect Game passed with score 300.\n")

    def test_spare(self):
        print("- Testing a Spare followed by a roll...")
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_multiple(17, 0)
        self.assertEqual(16, self.game.score(), "ERROR: Spare followed by 3 should have a score of 16")
        print("DONE: Spare followed by 3 passed with score 16.\n")

    def test_strike(self):
        print("- Testing a Strike followed by 3 and 4...")
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_multiple(16, 0)
        self.assertEqual(24, self.game.score(), "ERROR: Strike followed by 3 and 4 should have a score of 24")
        print("DONE: Strike followed by 3 and 4 passed with score 24.\n")

    def test_alternating_strikes_and_spares(self):
        print("- Testing alternating Strikes and Spares...")
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(7)
        self.game.roll(2)
        self.roll_multiple(14, 0)
        self.assertEqual(46, self.game.score(), "ERROR: Alternating Strikes and Spares should have a score of 46")
        print("DONE: Alternating Strikes and Spares passed with score 46.\n")

    def test_no_strikes_or_spares(self):
        print("- Testing game with no Strikes or Spares...")
        rolls = [1, 4, 4, 5, 6, 2, 7, 1, 3, 6, 4, 2, 5, 3, 6, 2, 4, 3, 2, 3]
        for pins in rolls:
            self.game.roll(pins)
        self.assertEqual(73, self.game.score(), "ERROR: Game with no strikes or spares should have a score of 73")
        print("DONE: Game with no strikes or spares passed with score 73.\n")

    def test_last_frame_spare(self):
        print("- Testing Spare in the last frame...")
        self.roll_multiple(18, 0)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(7)
        self.assertEqual(17, self.game.score(), "ERROR: Last frame spare should have a score of 17")
        print("DONE: Last frame spare passed with score 17.\n")

    def test_last_frame_strike(self):
        print("- Testing Strike in the last frame...")
        self.roll_multiple(18, 0)
        self.game.roll(10)
        self.game.roll(7)
        self.game.roll(2)
        self.assertEqual(19, self.game.score(), "ERROR: Last frame strike should have a score of 19")
        print("DONE: Last frame strike passed with score 19.\n")

    def test_all_strikes_except_last_frame(self):
        print("- Testing 11 strikes followed by a 9...")
        self.roll_multiple(10, 10)
        self.game.roll(10)
        self.game.roll(9)
        self.assertEqual(299, self.game.score(), "ERROR: Game with 11 strikes and a 9 should have a score of 299")
        print("DONE: Game with 11 strikes and a 9 passed with score 299.\n")

    def test_spare_followed_by_strike(self):
        print("- Testing a Spare followed by a Strike...")
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_multiple(14, 0)
        self.assertEqual(44, self.game.score(), "ERROR: Spare followed by strike should have a score of 44")
        print("DONE: Spare followed by strike passed with score 44.\n")

    def test_all_zeros_until_last_frame(self):
        print("- Testing all zeros until last frame...")
        self.roll_multiple(18, 0)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(30, self.game.score(), "ERROR: All zeros until last frame should have a score of 30")
        print("DONE: All zeros until last frame passed with score 30.\n")

if __name__ == "__main__":
    unittest.main()
