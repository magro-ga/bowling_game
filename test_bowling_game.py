from bowling_game import BowlingGame

def test_perfect_game():
    game = BowlingGame()
    for _ in range(12):
        game.roll('X')
    result = game.score()
    expected = 300
    assert result == expected, f"Perfect Game: FAIL (Expected {expected}, Got {result})"
    print("Perfect Game: PASS")

def test_gutter_game():
    game = BowlingGame()
    for _ in range(20):
        game.roll(0)
    result = game.score()
    expected = 0
    assert result == expected, f"Gutter Game: FAIL (Expected {expected}, Got {result})"
    print("Gutter Game: PASS")

def test_mixed_game():
    game = BowlingGame()
    rolls = ['X', 7, '/', 9, 0, 'X', 0, 8, 8, '/', 0, 6, 'X', 'X', 'X', 8, 1]
    for roll in rolls:
        game.roll(roll)
    result = game.score()
    expected = 167
    assert result == expected, f"Mixed Game: FAIL (Expected {expected}, Got {result})"
    print("Mixed Game: PASS")

def test_tenth_frame():
    game = BowlingGame()
    rolls = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    for roll in rolls:
        game.roll(roll)
    result = game.score()
    expected = 300
    assert result == expected, f"Tenth Frame: FAIL (Expected {expected}, Got {result})"
    print("Tenth Frame: PASS")

def test_spare_game():
    game = BowlingGame()
    for _ in range(10):
        game.roll(5)
        game.roll('/')
    game.roll(5)  # Bonus roll
    result = game.score()
    expected = 150
    assert result == expected, f"Spare Game: FAIL (Expected {expected}, Got {result})"
    print("Spare Game: PASS")

if __name__ == "__main__":
    print("Starting Tests...")
    test_perfect_game()
    test_gutter_game()
    test_mixed_game()
    test_tenth_frame()
    test_spare_game()
    print("Tests Completed!")