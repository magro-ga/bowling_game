from bowling_game import BowlingGame
from frame import Frame
from roll import Roll

new_game = BowlingGame()
new_game.execute()

for frame in new_game.frames:
    print(frame.to_string())

print(f"Total Score: {new_game.total_score()}")


    



