# Bowling Game

## Overview
This project implements a bowling game scoring system. The game accepts inputs for the number of pins knocked down in each roll.

## How It Works

### Core Class: `BowlingGame`
- **Purpose**: Tracks the game's frames and calculates the total score according to bowling rules.

### Bowling Rules Implemented
- A game consists of 10 frames, each with up to two rolls unless a strike occurs.
- A strike means 10 pins knocked down on the first roll.
- A spare means 10 pins knocked down over two rolls in a frame.
- The 10th frame can have up to three rolls if a strike or spare is rolled.

## Scoring

### Basic Scoring
- Each pin knocked down is worth 1 point.
- The score for each frame is the total number of pins knocked down in that frame.

### Strikes
- A strike is when all 10 pins are knocked down on the first roll of a frame.
- The score for a strike frame is 10 plus the total number of pins knocked down in the next two rolls.

### Spares
- A spare is when all 10 pins are knocked down in two rolls of a frame.
- The score for a spare frame is 10 plus the number of pins knocked down in the next roll.

### 10th Frame
- The 10th frame can have up to three rolls if a strike or spare is rolled.
- The score for the 10th frame includes any bonus rolls.

## Design Pattern

### State Pattern

The State Pattern is used to manage the different states of a frame (e.g., open frame, spare, strike). Each state has its own logic for calculating the score and transitioning to the next state.

### States Mapped

1. **OpenFrame**: Represents a frame where neither a strike nor a spare has been scored.
2. **SpareFrame**: Represents a frame where a spare has been scored.
3. **StrikeFrame**: Represents a frame where a strike has been scored.

### Why Use the State Pattern?

- **Clarity and Maintenance**: Isolates the logic for each state, making the code easier to understand and modify.
- **Extensibility**: Allows for easy addition of new states without modifying existing code.
- **Simplified Debugging and Testing**: Encapsulates state-specific behavior, making it easier to test each state independently.

### Why Not Use Other Patterns?

- **Strategy Pattern**: Not suitable as the game's states are fixed and predictable.
- **Template Method Pattern**: Does not provide the same level of flexibility and clarity for handling state transitions.
- **Observer Pattern**: Adds unnecessary complexity for handling the states of a bowling game frame.

## Running Tests and VS Code Configuration

To execute the tests or simulate, run the Python script and ensure that Visual Studio Code can find the modules correctly when running the debug, create a settings.json file in the .vscode directory with the following content:
```bash
python3 debug.py
python3 -m unittest test.bowling_game_test

{
    "python.analysis.extraPaths": [
        "./lib"
    ]
}