# Bowling Game

## Overview
This project implements a bowling game scoring system. The game accepts inputs for the number of pins knocked down in each roll, including special characters for strikes ('X') and spares ('/').

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
  7. `convert_input(pins)`: Converts input characters ('X' and '/') to pin numbers.

### Bowling Rules Implemented
- A game consists of 10 frames, each with up to two rolls unless a strike occurs.
- A strike ('X') means 10 pins knocked down on the first roll.
- A spare ('/') means 10 pins knocked down over two rolls in a frame.
- The 10th frame can have up to three rolls if a strike or spare is rolled.

## Features
- Accepts 'X' for strikes (10 pins).
- Accepts '/' for spares (remaining pins to make 10).
- Calculates the total score of the game.

## Design Pattern
We used the **State Pattern** to handle the different states of a frame (strike, spare, normal). This pattern was chosen because:
- It provides clarity and ease of maintenance by isolating the logic for each state.
- It allows for easy extensibility if new states need to be added.
- It simplifies debugging and testing by encapsulating state-specific behavior.

Other patterns like Strategy, Template Method, and Observer were not used because they either do not fit the fixed and predictable nature of the game's states or add unnecessary complexity.


## Tests
The implementation includes several predefined tests to validate the game's scoring system. Each test prints the result (PASS/FAIL) with the expected and actual scores for transparency.

## Test Cases
1. **Perfect Game**: All strikes.
   - Example rolls: `['X'] * 12`
   - Expected score: 300
   - Example output: `Perfect Game: PASS`

2. **Gutter Game**: All rolls knock down 0 pins.
   - Example rolls: `[0] * 20`
   - Expected score: 0
   - Example output: `Gutter Game: PASS`

3. **Mixed Game**: A mix of strikes, spares, and normal rolls.
   - Example rolls: `['X', 7, '/', 9, 0, 'X', 0, 8, 8, '/', 0, 6, 'X', 'X', 'X', 8, 1]`
   - Expected score: 167
   - Example output: `Mixed Game: PASS`

4. **10th Frame Bonus**: All strikes in the 10th frame.
   - Example rolls: `['X'] * 12`
   - Expected score: 300
   - Example output: `Tenth Frame: PASS`

5. **Spare Game**: Every frame is a spare with 5 pins each roll.
   - Example rolls: `[5, '/'] * 10 + [5]`
   - Expected score: 150
   - Example output: `Spare Game: PASS`

### Running Tests
To execute the tests, run the Python script:
```bash
python test_bowling_game.py