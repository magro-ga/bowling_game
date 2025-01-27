class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        """Records the number of pins knocked down in a throw."""
        pins = self.convert_input(pins)
        if not self.frames or len(self.frames[-1]) == 2 or sum(self.frames[-1]) == 10:
            self.frames.append([pins])
        else:
            self.frames[-1].append(pins)

    def convert_input(self, pins):
        """Converts input characters to pin numbers."""
        if pins == 'X':
            return 10
        elif pins == '/':
            return 10 - self.frames[-1][0]
        else:
            return int(pins)

    def score(self):
        """Calculates the total score of the game."""
        total_score = 0
        for i in range(10):  # Max 10 frames
            frame = self.frames[i]
            if self.is_strike(frame):  # Strike
                total_score += 10 + self.strike_bonus(i)
            elif self.is_spare(frame):  # Spare
                total_score += 10 + self.spare_bonus(i)
            else:  # Normal frame
                total_score += sum(frame)
        return total_score

    def is_strike(self, frame):
        """Checks if the frame was a strike."""
        return len(frame) == 1 and frame[0] == 10

    def is_spare(self, frame):
        """Checks if the frame was a spare."""
        return len(frame) == 2 and sum(frame) == 10

    def strike_bonus(self, frame_index):
        """Calculates the bonus of a strike."""
        next_frames = self.frames[frame_index + 1:]
        rolls = [roll for frame in next_frames for roll in frame]
        return sum(rolls[:2])

    def spare_bonus(self, frame_index):
        """Calculates the bonus of a spare."""
        if frame_index + 1 < len(self.frames):
            return self.frames[frame_index + 1][0]
        return 0