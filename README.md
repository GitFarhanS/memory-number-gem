# Number Pad Game

## Description
Number Pad Game is a fun and interactive game where the player must enter numbers displayed on a sliding number display. The objective is to correctly enter the numbers before they disappear from the screen. The game includes a scoring system to keep track of the player's performance.

## Features
- Sliding number display that generates random numbers with increasing digits.
- Interactive number pad with buttons for digits 0-9, delete, and enter.
- Text box to show the player's input.
- Scoring system to track correct entries.
- Visual feedback for correct and incorrect entries with screen flashes.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Ensure you have Python 3.x installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
2. Install the Pygame library using pip:
   ```bash
   pip install pygame

## Usage
1. Clone or download the repository.
2. Navigate to the directory containing the `mem_number.py` file.
3. Run the game using the following command:
   ```bash
   python number_pad_game.py

## How to Play

- When the game starts, a random number will slide across the screen from right to left.
- Use the number pad buttons to enter the displayed number into the text box.
- Click the "Enter" button to check if your input matches the displayed number.
  - If the input is correct, the screen will flash green, the score will increase, and a new number with more digits will appear.
  - If the input is incorrect, the screen will flash red and you can try again.
- Use the "Del" button to delete the last digit entered.
- The game continues indefinitely, with the difficulty increasing as the number of digits increases.


[![Example Gameplay Video](https://raw.githubusercontent.com/GitFarhanS/memory-number-gem/main/exampleInGIF.gif)](https://github.com/GitFarhanS/memory-number-gem/blob/main/exampleGameply.mp4)


## Classes and Functions

### Button
Represents a button on the number pad.
- `__init__(self, x, y, width, height, color, text, action=None)`: Initializes a button with position, size, color, text, and an optional action.
- `draw(self, surface)`: Draws the button on the screen.
- `is_clicked(self, pos)`: Checks if the button is clicked.

### SlidingNumberDisplay
Manages the sliding number display.
- `__init__(self, screen, width, height, font)`: Initializes the sliding number display.
- `draw(self)`: Draws the current number on the screen.
- `reset(self)`: Resets the display with a new random number.
- `get_value(self)`: Returns the current number as a string.

### Score
Manages the game score.
- `__init__(self, x, y, font)`: Initializes the score display.
- `draw(self, surface)`: Draws the score on the screen.
- `increase(self)`: Increases the score by one.
- `reset(self)`: Resets the score to zero.

### TextBox
Manages the text box for user input.
- `__init__(self, x, y, width, height, font)`: Initializes the text box.
- `draw(self, surface)`: Draws the text box on the screen.
- `update_text(self, new_text)`: Updates the text box with new input.
- `set_text(self, new_text)`: Sets the text box to a specific value.
- `get_text(self)`: Returns the current text in the text box.

### NumberPad
Main game class.
- `__init__(self)`: Initializes the game components.
- `create_buttons(self)`: Creates the buttons for the number pad.
- `run(self)`: Main game loop.
- `flash_screen(self, color, duration=0.2)`: Flashes the screen with a specified color for visual feedback.
- `update_text_box(self, text)`: Updates the text box with new input.
- `set_text(self, text)`: Sets the text box to a specific value.
- `get_text(self)`: Returns the current text in the text box.
- Button action methods (`button_1_action`, `button_2_action`, etc.): Actions for each button press.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


## Acknowledgements
This game was developed using the Pygame library. Special thanks to the Pygame community for their contributions and support.

