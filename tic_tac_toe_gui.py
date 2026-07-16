"""
Tic-Tac-Toe - GUI version (Tkinter)

A clickable graphical version of the console Tic-Tac-Toe game.
Run this file directly: python tic_tac_toe_gui.py
"""

import tkinter as tk

# ---- Global counters (tracked across all games played this session) ----
games_played = 0
x_wins = 0
o_wins = 0
draws = 0
move_count = 0

# ---- Global game state ----
board = [' '] * 9
current_player = 'X'
buttons = []
game_over = False


def check_winner(board):
    """
    Check the board for a win or draw. Same logic as the console version.

    Parameters:
        board (list): current board state.

    Returns:
        str or None: 'X' or 'O' if that player has won, 'Draw' if the board
        is full with no winner, otherwise None (game continues).
    """
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]

    for a, b, c in winning_combinations:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]

    if ' ' not in board:
        return 'Draw'

    return None


def update_stats_label():
    """Refresh the statistics label with the current global counter values."""
    stats_label.config(
        text=(f"Games: {games_played}  |  X wins: {x_wins}  |  "
              f"O wins: {o_wins}  |  Draws: {draws}  |  Moves: {move_count}")
    )


def disable_all_buttons():
    """Disable every board button, used once a game has ended."""
    for button in buttons:
        button.config(state='disabled')


def on_button_click(index):
    """
    Handle a player clicking a board cell.

    Parameters:
        index: the 0-8 board position that was clicked.
    """
    global current_player, move_count, games_played, x_wins, o_wins, draws, game_over

    if game_over or board[index] != ' ':
        return  # ignore clicks on taken cells or after the game has ended

    board[index] = current_player
    move_count += 1
    buttons[index].config(
        text=current_player,
        fg='#2563eb' if current_player == 'X' else '#dc2626',
        state='disabled'
    )

    result = check_winner(board)

    if result in ('X', 'O'):
        games_played += 1
        if result == 'X':
            x_wins += 1
        else:
            o_wins += 1
        status_label.config(text=f"Player {result} wins!")
        game_over = True
        disable_all_buttons()
    elif result == 'Draw':
        games_played += 1
        draws += 1
        status_label.config(text="It's a draw!")
        game_over = True
    else:
        current_player = 'O' if current_player == 'X' else 'X'
        status_label.config(text=f"Player {current_player}'s turn")

    update_stats_label()


def reset_board():
    """Clear the board and start a new round without resetting statistics."""
    global board, current_player, game_over

    board = [' '] * 9
    current_player = 'X'
    game_over = False

    for button in buttons:
        button.config(text='', state='normal', fg='black')

    status_label.config(text="Player X's turn")


def build_window():
    """Construct the Tkinter window, board buttons, and labels."""
    global buttons, status_label, stats_label

    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    status_label = tk.Label(window, text="Player X's turn", font=("Arial", 14))
    status_label.grid(row=0, column=0, columnspan=3, pady=10)

    buttons = []
    for i in range(9):
        # The lambda default argument (index=i) captures each button's own position at creation time - without it, every button would end up calling on_button_click with the same final value of i.
        button = tk.Button(
            window, text='', font=("Arial", 24), width=4, height=2,
            command=lambda index=i: on_button_click(index)
        )
        button.grid(row=1 + i // 3, column=i % 3)
        buttons.append(button)

    stats_label = tk.Label(window, text="", font=("Arial", 10))
    stats_label.grid(row=4, column=0, columnspan=3, pady=5)
    update_stats_label()

    new_game_button = tk.Button(window, text="New Game", command=reset_board)
    new_game_button.grid(row=5, column=0, columnspan=3, pady=10)

    return window


def main():
    """Entry point: build the window and start the Tkinter event loop."""
    window = build_window()
    window.mainloop()


if __name__ == "__main__":
    main()
