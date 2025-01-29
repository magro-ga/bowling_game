class ScoreCalculator:
    def __init__(self, frames):
        self.frames = frames

    def calculate(self):
        total_score = 0

        for index, frame in enumerate(self.frames):
            frame_score = frame.total_pins()

            if frame.is_strike() and index < 9:
                frame_score += self.strike_bonus(index)
            elif frame.is_spare() and index < 9:
                frame_score += self.spare_bonus(index)

            total_score += frame_score

        return total_score

    def strike_bonus(self, index):
        next_frame = self.frames[index + 1] if index + 1 < len(self.frames) else None
        if not next_frame:
            return 0

        if index == 9:
            return sum(next_frame.rolls[:2])

        bonus_rolls = next_frame.rolls_with_default()

        if next_frame.is_strike() and index < 8:
            second_frame = self.frames[index + 2] if index + 2 < len(self.frames) else None
            if second_frame:
                bonus_rolls += second_frame.rolls_with_default()

        return sum(bonus_rolls[:2])

    def spare_bonus(self, index):
        next_frame = self.frames[index + 1] if index + 1 < len(self.frames) else None
        if not next_frame or not next_frame.rolls_with_default():
            return 0

        return next_frame.rolls_with_default()[0]
