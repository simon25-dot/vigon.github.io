import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, window, player_name, computer_level):
        self.window = window
        self.window.title("GROUP 5")
        self.window.geometry("800x900")
        self.window.configure(bg="lightslategrey")

        self.player_name = player_name

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(window, text="", font=("Helvetica", 20), width=8, height=4, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.reset_button = tk.Button(window, text="Reset", command=self.reset_game, font=("Helvetica", 14), bg="orange", fg="black")
        self.reset_button.grid(row=3, columnspan=3, pady=10)

        self.level_menu_label = tk.Label(window, text="Select Computer Level:", font=("fantasy", 12), bg="#F5F5DC", fg="dark green")
        self.level_menu_label.grid(row=4, columnspan=3, pady=5)

        self.computer_level_var = tk.StringVar()
        self.computer_level_var.set(computer_level)

        self.level_menu = tk.OptionMenu(window, self.computer_level_var, "Easy", "Medium", "Hard")
        self.level_menu.grid(row=5, columnspan=3, pady=5)

        self.print_welcome_animation()

    def print_welcome_animation(self):
        welcome_label = tk.Label(self.window, text="", font=("Copperplate, Papyrus, fantasy", 18, "bold"), bg="#F5F5DC", fg="dark green")
        welcome_label.grid(row=9, columnspan=3, pady=20) 

        def change_color_and_position(current_color_index, y_position):
            colors = ["darkgreen","gray", "aqua"] 
            current_color = colors[current_color_index]
            welcome_label.config(text=f"Welcome to Group five's game, {self.player_name}! Enjoy", fg=current_color)
            welcome_label.place(y=y_position, x=200) 
            current_color_index = (current_color_index + 1) % len(colors)
            y_position += 10  
            if y_position < 700:
                self.window.after(800, change_color_and_position, current_color_index, y_position)
        def color_change(color_index):
            color = ["darkgreen","green","aqua"]
            color_index = (color_index +1) %len(color)
            current_color = color[color_index]
            welcome_label.config(fg=current_color)
            self.window.after(1000, color_change,color_index,)
            
            change_color_and_position(0, 0)
            color_change(0)

        change_color_and_position(0, 0)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled", disabledforeground="black", bg="gray" if self.current_player == "X" else "burlywood")
            if self.check_winner():
                if self.current_player == "X":
                    messagebox.showinfo("Congratulations!", f"{self.player_name}, you win!😎")
                else:
                    messagebox.showinfo("Oops!", f"{self.player_name}, you lose. Try again next time😰!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tie!",f"{self.player_name},What a tough game😑!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.make_computer_move()

    def make_computer_move(self):
        level = self.computer_level_var.get()
        if level == "Easy":
            self.make_random_move()
        elif level == "Medium":
            self.make_medium_move()
        elif level == "Hard":
            self.make_hard_move()

    def make_random_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ""]
        if available_moves:
            move = random.choice(available_moves)
            row, col = divmod(move, 3)
            self.make_move(row, col)

    def make_medium_move(self):
        for i in range(9):
            if self.board[i] == "":
                temp_board = self.board.copy()
                temp_board[i] = "O"
                if self.check_winner(temp_board, player="O"):
                    row, col = divmod(i, 3)
                    self.make_move(row, col)
                    return

        for i in range(9):
            if self.board[i] == "":
                temp_board = self.board.copy()
                temp_board[i] = "X"
                if self.check_winner(temp_board, player="X"):
                    row, col = divmod(i, 3)
                    self.make_move(row, col)
                    return

        self.make_random_move()

    def make_hard_move(self):
        self.make_medium_move()

    def check_winner(self, board=None, player=None):
        if board is None:
            board = self.board
        if player is None:
            player = self.current_player

        for i in range(3):
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
                self.highlight_winner(i * 3, i * 3 + 1, i * 3 + 2)
                return True

        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] == player:
                self.highlight_winner(i, i + 3, i + 6)
                return True

        if board[0] == board[4] == board[8] == player:
            self.highlight_winner(0, 4, 8)
            return True
        if board[2] == board[4] == board[6] == player:
            self.highlight_winner(2, 4, 6)
            return True

        return False

    def highlight_winner(self, *positions):
        for pos in positions:
            row, col = divmod(pos, 3)
            self.buttons[row][col].config(bg="green", fg="white")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", bg="#F5F5DC", fg="black")
        self.current_player = "X"
        self.board = [""] * 9

def start_game():
    player_name = player_entry.get()
    computer_level = computer_level_var.get()

    if player_name:
        game_window = tk.Toplevel(root)
        game_window.configure(bg="#F5F5DC")
        TicTacToe(game_window, player_name, computer_level)
        start_frame.destroy()
    else:
        messagebox.showwarning("Warning", "Please enter your name.")

root = tk.Tk()
root.configure(bg="white")

start_frame = tk.Frame(root, bg="#F5F5DC")
start_frame.pack(pady=50)

player_label = tk.Label(start_frame, text="Your Name:", font=("Helvetica", 12), bg="#F5F5DC", fg="dark green")
player_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
player_entry = tk.Entry(start_frame, font=("Helvetica", 12))
player_entry.grid(row=0, column=1, padx=10, pady=5)

computer_level_label = tk.Label(start_frame, text="Select Computer Level:", font=("Helvetica", 12), bg="#F5F5DC", fg="dark green")
computer_level_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
computer_level_var = tk.StringVar()
computer_level_var.set("Easy")
computer_level_menu = tk.OptionMenu(start_frame, computer_level_var, "Easy", "Medium", "Hard")
computer_level_menu.grid(row=1, column=1, padx=10, pady=5)

start_button = tk.Button(start_frame, text="Begin", command=start_game, font=("Helvetica", 14), bg="orange", fg="black")
start_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()

  
  
  