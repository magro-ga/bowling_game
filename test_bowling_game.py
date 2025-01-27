from bowling_game import BowlingGame, bowling_score

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

def test_alternating_strike_spare():
    game = BowlingGame()
    rolls = ['X', 5, '/', 'X', 5, '/', 'X', 5, '/', 'X', 5, '/', 'X', 5, '/', 'X', 5, '/', 'X', 5, '/', 'X']
    for roll in rolls:
        game.roll(roll)
    result = game.score()
    expected = 200
    assert result == expected, f"Alternating Strike and Spare: FAIL (Expected {expected}, Got {result})"
    print("Alternating Strike and Spare: PASS")

def test_all_spares_different_pins():
    game = BowlingGame()
    rolls = [3, '/', 4, '/', 5, '/', 6, '/', 7, '/', 8, '/', 9, '/', 2, '/', 1, '/', 0, '/']
    for roll in rolls:
        game.roll(roll)
    game.roll(5)  # Bonus roll
    result = game.score()
    expected = 147
    assert result == expected, f"All Spares with Different Pins: FAIL (Expected {expected}, Got {result})"
    print("All Spares with Different Pins: PASS")

def test_edge_case_mixed():
    game = BowlingGame()
    rolls = [0, 0, 'X', 0, 0, 5, 5, 0, 0, 'X', 0, 0, 'X', 'X', 'X', 'X', 'X', 'X']
    for roll in rolls:
        game.roll(roll)
    result = game.score()
    expected = 120
    assert result == expected, f"Edge Case Mixed: FAIL (Expected {expected}, Got {result})"
    print("Edge Case Mixed: PASS")

def test_bowling_score():
    assert bowling_score('X X X X X X X X X XXX') == 300, "Perfect Game: FAIL"
    assert bowling_score('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-') == 90, "All Nines: FAIL"
    assert bowling_score('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5') == 150, "All Spares: FAIL"
    assert bowling_score('X 7/ 9- X -8 8/ -6 X X X81') == 167, "Mixed Game: FAIL"
    print("bowling_score tests: PASS")

if __name__ == "__main__":
    print("Starting Tests...")
    test_perfect_game()
    test_gutter_game()
    test_mixed_game()
    test_spare_game()
    test_alternating_strike_spare()
    test_all_spares_different_pins()
    test_edge_case_mixed()
    test_bowling_score()
    print("Tests Completed!")