class ScoreCalculator:
    def __init__(self, frames):
        self.frames = frames

    def calculate(self):
        total_score = 0

        for index, frame in enumerate(self.frames):
            frame_score = sum(frame.rolls)

            if frame.is_strike() and index < 9:
                frame_score += self.strike_bonus(index)
            elif frame.is_spare() and index < 9:
                frame_score += self.spare_bonus(index)

            total_score += frame_score

        return total_score

    def strike_bonus(self, index):
        if index >= 9:
            return 0

        next_frame = self.frames[index + 1]
        if not next_frame.rolls:
                return 0

        if next_frame.is_strike() and index < 8:
            second_frame = self.frames[index + 2] if index + 2 < len(self.frames) else None
            second_bonus = second_frame.rolls[0] if second_frame and second_frame.rolls else 0
            return next_frame.rolls[0] + second_bonus
        else:
            return sum(next_frame.rolls[:2]) if len(next_frame.rolls) >= 2 else next_frame.rolls[0]

    def spare_bonus(self, index):
        if index >= 9:
            return 0

        next_frame = self.frames[index + 1]
        return next_frame.rolls[0] if next_frame and next_frame.rolls else 0
