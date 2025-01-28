# Bowling Game

## Overview
This project implements a bowling game scoring system. The game accepts inputs for the number of pins knocked down in each roll, including special characters for strikes ('X') and spares ('/').

## How It Works

### Core Class: `BowlingGame`
- **Purpose**: Tracks the game's frames and calculates the total score according to bowling rules.

### Bowling Rules Implemented
- A game consists of 10 frames, each with up to two rolls unless a strike occurs.
- A strike ('X') means 10 pins knocked down on the first roll.
- A spare ('/') means 10 pins knocked down over two rolls in a frame.
- The 10th frame can have up to three rolls if a strike or spare is rolled.

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

### Running Tests

To execute the tests, run the Python script:
```bash
python test_bowling_game.py