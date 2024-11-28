import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.difficulty = 'Medium'  # Default difficulty
        self.score_x = 0
        self.score_o = 0
        self.draws = 0  # Draw count
        
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Player 'X' starts the game
        self.buttons = [None] * 9  # To hold the button references
        
        self.create_menu()
        self.create_buttons()
        self.create_score_display()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        settings_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Settings", menu=settings_menu)
        
        # Difficulty sub-menu
        difficulty_menu = tk.Menu(settings_menu, tearoff=0)
        settings_menu.add_cascade(label="Set Difficulty", menu=difficulty_menu)
        difficulty_menu.add_command(label="Easy", command=lambda: self.set_difficulty("Easy"))
        difficulty_menu.add_command(label="Medium", command=lambda: self.set_difficulty("Medium"))
        difficulty_menu.add_command(label="Hard", command=lambda: self.set_difficulty("Hard"))
        
        # Reset Score option
        settings_menu.add_command(label="Reset Score and Start New Game", command=self.reset_score)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        messagebox.showinfo("Difficulty Set", f"Difficulty set to {self.difficulty}")

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Arial 24', width=6, height=3,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button

    def create_score_display(self):
        self.score_label = tk.Label(
            self.root,
            text=f"X Wins: {self.score_x} | O Wins: {self.score_o} | Draws: {self.draws}",
            font='Arial 16'
        )
        self.score_label.grid(row=3, column=0, columnspan=3)

    def player_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.is_winner(self.current_player):
                self.show_winner(self.current_player)
            elif self.is_draw():
                self.show_draw()
            else:
                self.current_player = 'O'
                self.ai_move()

    def ai_move(self):
        move = self.best_move()
        self.board[move] = 'O'
        self.buttons[move].config(text='O')
        if self.is_winner('O'):
            self.show_winner('O')
        elif self.is_draw():
            self.show_draw()
        else:
            self.current_player = 'X'

    def is_winner(self, player):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def is_draw(self):
        return ' ' not in self.board

    def show_winner(self, player):
        if player == 'X':
            self.score_x += 1
        else:
            self.score_o += 1
        self.update_score_display()
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_draw(self):
        self.draws += 1
        self.update_score_display()
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def update_score_display(self):
        self.score_label.config(text=f"X Wins: {self.score_x} | O Wins: {self.score_o} | Draws: {self.draws}")

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

    def reset_score(self):
        self.score_x = 0
        self.score_o = 0
        self.draws = 0
        self.update_score_display()
        self.reset_game()

    def minimax(self, depth, is_maximizing):
        if self.is_winner('X'):
            return -10 + depth
        if self.is_winner('O'):
            return 10 - depth
        if self.is_draw():
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.board[move] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def best_move(self):
        if self.difficulty == 'Easy':
            return self.random_move()
        elif self.difficulty == 'Medium':
            if random.random() < 0.5:  # 50% chance to play randomly
                return self.random_move()
            else:  # Otherwise, play optimally
                return self.best_hard_move()
        else:  # Hard
            return self.best_hard_move()

    def best_hard_move(self):
        best_score = float('-inf')
        move = -1
        for i in self.available_moves():
            self.board[i] = 'O'
            score = self.minimax(0, False)
            self.board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
        return move

    def random_move(self):
        return random.choice(self.available_moves())

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Expanded window size
    game = TicTacToe(root)
    root.mainloop()
