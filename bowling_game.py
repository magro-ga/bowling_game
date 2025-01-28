import random
from frame import Frame
from roll import Roll

class BowlingGame:
    def __init__(self):
        self.frames = []

    def execute(self):
        for i in range(10):
            new_frame = Frame(i + 1)
            if i == 9:
                new_frame.rolls = [Roll(), Roll(), Roll()]
            else:
                new_frame.rolls = [Roll(), Roll()]
            self.frames.append(new_frame)

        for i in range(10):
            current_frame = self.frames[i]
            for roll_index, roll in enumerate(current_frame.rolls):
                if roll_index == 0:
                    roll.pins = random.randint(0, 10)
                    if roll.pins == 10 and i != 9:
                        break
                else:
                    remaining_pins = 10 - sum(roll.pins for roll in current_frame.rolls[:roll_index])
                    roll.pins = random.randint(0, remaining_pins)
                    if roll_index == 1 and current_frame.rolls[0].pins + roll.pins == 10 and i != 9:  # Spare e não é o último frame
                        break

            if i == 9:
                if self.is_strike(current_frame) or self.is_spare(current_frame):
                    current_frame.rolls[2].pins = random.randint(0, 10)
                else:
                    current_frame.rolls[2].pins = 0

            if self.is_strike(current_frame):
                current_frame.type = "strike"
                current_frame.score = 10 + self.strike_bonus(i)
            elif self.is_spare(current_frame):
                current_frame.type = "spare"
                current_frame.score = 10 + self.spare_bonus(i)
            else:
                current_frame.type = "open"
                current_frame.score = sum(roll.pins for roll in current_frame.rolls[:2])

        total_score = 0
        for i, frame in enumerate(self.frames):
            if i == 9 and (frame.type == "strike" or frame.type == "spare"):
                frame.score = sum(roll.pins for roll in frame.rolls)
            else:
                if frame.type == "strike":
                    frame.score += self.strike_bonus(i)
                elif frame.type == "spare":
                    frame.score += self.spare_bonus(i)
            total_score += frame.score
            print(f"Frame {i+1}: {frame.type.capitalize()} - Score: {total_score}")
        print(f"Total Score: {total_score}")

    def is_strike(self, frame):
        return len(frame.rolls) > 0 and frame.rolls[0].pins == 10

    def is_spare(self, frame):
        return len(frame.rolls) > 1 and frame.rolls[0].pins + frame.rolls[1].pins == 10

    def strike_bonus(self, frame_index):
        next_rolls = []
        for i in range(frame_index + 1, min(frame_index + 3, 10)):
            next_rolls.extend(self.frames[i].rolls)
        return sum(roll.pins for roll in next_rolls[:2])

    def spare_bonus(self, frame_index):
        next_frames = self.frames[frame_index + 1:]
        if next_frames:
            return next_frames[0].rolls[0].pins
        return 0

    def total_score(self):
        return sum(frame.score for frame in self.frames)