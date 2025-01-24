class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        """Records the number of pins knocked down in a throw."""
        if not self.frames or len(self.frames[-1]) == 2 or sum(self.frames[-1]) == 10:
            self.frames.append([pins])
        else:
            self.frames[-1].append(pins)

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
        bonus = 0
        next_frames = self.frames[frame_index + 1:]
        rolls = [roll for frame in next_frames for roll in frame]
        bonus += sum(rolls[:2])
        return bonus

    def spare_bonus(self, frame_index):
        """Calculates the bonus of a sparegame = BowlingGame()
        for _ in range(12):
            game.roll(10)
        if game.score() != 300:
            print(f"Test Perfect Game Failed: Expected 300, got {game.score()}")
        else:
            print("Test Perfect Game Passed!")."""
        if frame_index + 1 < len(self.frames):
            return self.frames[frame_index + 1][0]
        return 0

# Tests
if __name__ == "__main__":
    def test_perfect_game():
        game = BowlingGame()
        for _ in range(12):
            game.roll(10)
        result = game.score()
        expected = 300
        if result == expected:
            print("Perfect Game: PASS")
        else:
            print(f"Perfect Game: FAIL (Expected {expected}, Got {result})")

    def test_gutter_game():
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)
        result = game.score()
        expected = 0
        if result == expected:
            print("Gutter Game: PASS")
        else:
            print(f"Gutter Game: FAIL (Expected {expected}, Got {result})")

    def test_mixed_game():
        game = BowlingGame()
        rolls = [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]
        for roll in rolls:
            game.roll(roll)
        result = game.score()
        expected = 167
        if result == expected:
            print("Mixed Game: PASS")
        else:
            print(f"Mixed Game: FAIL (Expected {expected}, Got {result})")

    def test_tenth_frame():
        game = BowlingGame()
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        for roll in rolls:
            game.roll(roll)
        result = game.score()
        expected = 300
        if result == expected:
            print("Tenth Frame: PASS")
        else:
            print(f"Tenth Frame: FAIL (Expected {expected}, Got {result})")


    def test_spare_game():
        game = BowlingGame()
        for _ in range(10):
            game.roll(5)
            game.roll(5)  # Spare every frame
        game.roll(5)  # Bonus roll
        result = game.score()
        expected = 150
        if result == expected:
            print("Spare Game: PASS")
        else:
            print(f"Spare Game: FAIL (Expected {expected}, Got {result})")

    print("Iniciando os testes...")
    test_perfect_game()
    test_gutter_game()
    test_mixed_game()
    test_tenth_frame()
    test_spare_game()
    print("Testes finalizados!")