# Tic-Tac-Toe (Python)

A two-player Tic-Tac-Toe game built for the Rockborne Python Game Development project. Includes a console version and a bonus Tkinter GUI version, both built on the same core game logic.

## Files

| File | Description |
|---|---|
| `Python_04_01_Project_PythonGameDevelopment.ipynb` | Main project notebook — flowchart, console game, and GUI code |
| `Flowchart.png` | Game logic flowchart |
| `tic_tac_toe_gui.py` | Standalone script for the Tkinter GUI version |

## How to Play

### Console version (in the notebook)

1. Open `Python_04_01_Project_PythonGameDevelopment.ipynb` in Jupyter or VS Code.
2. Make sure the notebook is running a **Python** kernel (not Julia — check the kernel picker in the top-right).
3. Run the "Part Two" code cell.
4. When prompted, enter a number from **1–9** to place your mark on the corresponding board position:
   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```
5. Players alternate turns (X goes first). Invalid input (non-numeric, out of range, or an already-taken cell) is rejected and re-prompted.
6. After a win or draw, you'll be asked "Play again? (y/n)". Answering anything other than `y` ends the session and prints final statistics.

### GUI version

1. Run `tic_tac_toe_gui.py` directly:
   ```
   python tic_tac_toe_gui.py
   ```
2. Click any empty square to place your mark. X and O alternate automatically and are shown in different colors.
3. A status label at the top shows whose turn it is, and announces the winner or a draw.
4. Click **New Game** to start a new round without resetting the running statistics.
5. Statistics (games played, X wins, O wins, draws, total moves) are shown live at the bottom of the window.

## Features

- Two playable versions sharing the same win/draw-checking logic (`check_winner`)
- Input validation: rejects non-numeric input, out-of-range numbers, and already-taken cells
- Global counters track statistics across multiple games in a session: games played, X wins, O wins, draws, total moves
- Modular design — the game logic is split into single-purpose functions (`print_board`, `get_valid_move`, `check_winner`, `play_round`, `show_stats`, `main`)

## Requirements

- Python 3.x
- `tkinter` (included with most standard Python installs) for the GUI version — no external packages needed

## Flowchart

See `Flowchart.png`, or view it embedded in the notebook's "Part One" section.
