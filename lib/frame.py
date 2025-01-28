class Frame:
    def __init__(self, last_frame=False):
        self.rolls = []
        self.is_last_frame = last_frame

    def add_roll(self, roll):
        if not self.is_last_frame and (len(self.rolls) >= 2 or (len(self.rolls) == 1 and self.rolls[0] == 10)):
            raise ValueError("Invalid roll: Frame is already complete")
        if self.is_last_frame and len(self.rolls) >= 3:
            raise ValueError("Invalid roll: Frame is already complete")

        self.rolls.append(roll)

    def is_complete(self):
        if self.is_last_frame:
            return len(self.rolls) == 3 or (len(self.rolls) == 2 and sum(self.rolls) < 10)
        return self.is_strike() or len(self.rolls) == 2

    def is_strike(self):
        return self.rolls and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) >= 2 and sum(self.rolls[:2]) == 10

    def remaining_pins(self):
        if self.is_last_frame:
            if len(self.rolls) == 1 and self.is_strike():
                return 10
            elif len(self.rolls) == 2 and self.is_strike():
                return 10
            elif len(self.rolls) == 2 and self.is_spare():
                return 10
            elif len(self.rolls) == 3:
                return 0
        return 10 - sum(self.rolls)
