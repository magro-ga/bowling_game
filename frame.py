class Frame:
    def __init__(self, id):
        self.id = id
        self.rolls = []
        self.type = None
        self.score = 0
        self.strike_in = None
        self.spare_in = None

    def to_string(self):
        if self.id == 10 and (self.type == "strike" or self.type == "spare"):
            r3_value = self.rolls[2].pins if len(self.rolls) > 2 else None
            return f"[{self.id}][{self.type}] - R1: {self.rolls[0].pins} - R2: {self.rolls[1].pins} - R3: {r3_value} - Score: {self.score}"
        else:
            return f"[{self.id}][{self.type}] - R1: {self.rolls[0].pins} - R2: {self.rolls[1].pins} - Score: {self.score}"