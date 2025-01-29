class Frame:
    def __init__(self, last_frame=False):
        self.rolls = []
        self.is_last_frame = last_frame

    def add_roll(self, pins):
        if self.is_complete():
            raise ValueError("Frame is now complete")

        if self.is_last_frame:
            self.rolls.append(pins)
            return

        if len(self.rolls) == 1:
            max_possible = 10 - self.rolls[0]
            if pins == 10:
                pins = 0
            pins = min(pins, max_possible)
        self.rolls.append(pins)

    def is_complete(self):
        if self.is_last_frame:
            return len(self.rolls) == 3 or (len(self.rolls) == 2 and sum(self.rolls) < 10)
        return self.is_strike() or len(self.rolls) == 2

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def total_pins(self):
        return sum(self.rolls)

    def rolls_with_default(self):
        if self.is_last_frame:
            return self.rolls

        if self.is_strike():
            return [10]

        if not self.rolls:
            return [0, 0]

        return self.rolls if len(self.rolls) == 2 else [self.rolls[0], 0]

    def __repr__(self):
        return f"Frame({self.rolls})"
