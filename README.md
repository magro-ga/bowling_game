# Bowling Game Implementation

This project implements a simple bowling game scoring system in Python. The program calculates the total score of a bowling game based on user input and tests its behavior through predefined scenarios.

## How It Works

### Core Class: `BowlingGame`
- **Purpose**: Tracks the game's frames and calculates the total score according to bowling rules.
- **Key Methods**:
  1. `roll(pins)`: Records the number of pins knocked down in a roll.
  2. `score()`: Calculates the total score of the game.
  3. `is_strike(frame)`: Checks if a frame is a strike (10 pins on the first roll).
  4. `is_spare(frame)`: Checks if a frame is a spare (10 pins over two rolls in the frame).
  5. `strike_bonus(frame_index)`: Calculates the bonus for a strike (next two rolls).
  6. `spare_bonus(frame_index)`: Calculates the bonus for a spare (next roll).

### Bowling Rules Implemented
- A game consists of 10 frames, each with up to two rolls unless a strike occurs.
- **Strike**: All 10 pins are knocked down in the first roll of a frame. Bonus: Pins knocked down in the next two rolls.
- **Spare**: All 10 pins are knocked down across two rolls of a frame. Bonus: Pins knocked down in the next roll.
- **10th Frame**: Special handling to allow up to three rolls if a strike or spare occurs.

### Edge Cases Covered
- Gutter Game: All rolls knock down 0 pins.
- Perfect Game: All rolls are strikes (score of 300).
- Mixed Game: Combination of strikes, spares, and normal rolls.

## Tests
The implementation includes several predefined tests to validate the game's scoring system. Each test prints the result (PASS/FAIL) with the expected and actual scores for transparency.

### Test Cases
1. **Perfect Game**: 12 strikes in a row.
   - Expected score: 300
   - Example output: `Perfect Game: PASS`

2. **Gutter Game**: All rolls score 0.
   - Expected score: 0
   - Example output: `Gutter Game: PASS`

3. **Mixed Game**: A mix of strikes, spares, and normal rolls.
   - Example rolls: `[10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]`
   - Expected score: 167
   - Example output: `Mixed Game: PASS`

4. **10th Frame Bonus**: All strikes in the 10th frame.
   - Expected score: 300
   - Example output: `Tenth Frame: PASS`

5. **Spare Game**: Every frame is a spare with 5 pins each roll.
   - Expected score: 150
   - Example output: `Spare Game: PASS`

### Running Tests
To execute the tests, run the Python script:
```bash
python bowling_game.py
```
The output will indicate whether each test passed or failed.

## Example Output
```
Iniciando os testes...
Perfect Game: PASS
Gutter Game: PASS
Mixed Game: PASS
Tenth Frame: PASS
Spare Game: PASS
Testes finalizados!
```