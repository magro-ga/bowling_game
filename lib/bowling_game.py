from frame import Frame
from score_calculator import ScoreCalculator

class BowlingGame:
    def __init__(self):
        self.frames = [Frame() for _ in range(9)] + [Frame(last_frame=True)]
        self.current_frame = 0

    def roll(self, pins):
        if self.game_over():
            raise Exception("Game is over")

        frame = self.current_frame_obj()
        frame.add_roll(pins)

        if frame.is_complete() and not self.is_last_frame():
            self.advance_frame()

    def score(self):
        return ScoreCalculator(self.frames).calculate()

    def current_frame_obj(self):
        return self.frames[self.current_frame]

    def advance_frame(self):
        self.current_frame += 1

    def game_over(self):
        last_frame = self.current_frame_obj()
        return (self.is_last_frame() and 
                (len(last_frame.rolls) == 3 or 
                 (not last_frame.is_strike() and not last_frame.is_spare() and last_frame.is_complete())))

    def is_last_frame(self):
        return self.current_frame == 9
