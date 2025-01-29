import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './lib')))

from bowling_game import BowlingGame

def debug_game(rolls, description):
    game = BowlingGame()
    print(f"\n=== {description} ===")

    for index, pins in enumerate(rolls):
        game.roll(pins)
        frame_rolls = [frame.rolls for frame in game.frames]
        print(f"Roll {index + 1}: Knocked down {pins} pins | Current Frame: {frame_rolls}")
        print(f"Partial Score: {game.score()}")
        print("-------------------------")

    print(f"Final Score: {game.score()}")
    print("===================================\n")

debug_game([10] * 12, "Perfect Game (12 strikes)")

debug_game([0] * 20, "Gutter Game (all rolls 0)")

debug_game([3, 6] * 10, "Regular Game (only low numbers)")

debug_game([5, 5] * 10 + [5], "Game with Only Spares (150 points)")

debug_game([10, 3, 6, 7, 3, 10, 2, 8, 6, 10, 10, 10, 5, 5, 10], "Testing Without a second roll")

debug_game([1, 4, 4, 5, 6, 2, 7, 1, 3, 6, 4, 2, 5, 3, 6, 2, 4, 3, 2, 3], "Random Game 2")

debug_game([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9], "Random Game 3")
