import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x500")
        
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        title_label = tk.Label(self.root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        instructions = tk.Label(self.root, text="Choose your move:", font=("Arial", 12))
        instructions.pack(pady=5)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, 
                                command=lambda: self.play_game("rock"))
        self.rock_btn.grid(row=0, column=0, padx=10)
        
        self.paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10,
                                 command=lambda: self.play_game("paper"))
        self.paper_btn.grid(row=0, column=1, padx=10)
        
        self.scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10,
                                    command=lambda: self.play_game("scissors"))
        self.scissors_btn.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        
        score_frame = tk.Frame(self.root)
        score_frame.pack(pady=10)
        
        tk.Label(score_frame, text="Your Score:", font=("Arial", 12)).grid(row=0, column=0)
        self.user_score_label = tk.Label(score_frame, text="0", font=("Arial", 12))
        self.user_score_label.grid(row=0, column=1, padx=10)
        
        tk.Label(score_frame, text="Computer Score:", font=("Arial", 12)).grid(row=1, column=0)
        self.computer_score_label = tk.Label(score_frame, text="0", font=("Arial", 12))
        self.computer_score_label.grid(row=1, column=1, padx=10)
        
        tk.Label(score_frame, text="Ties:", font=("Arial", 12)).grid(row=2, column=0)
        self.ties_label = tk.Label(score_frame, text="0", font=("Arial", 12))
        self.ties_label.grid(row=2, column=1, padx=10)
        
        reset_btn = tk.Button(self.root, text="Reset Game", font=("Arial", 12),
                             command=self.reset_game)
        reset_btn.pack(pady=20)
    
    def play_game(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        if user_choice == computer_choice:
            result = "It's a tie!"
            self.ties += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = f"You win! {user_choice.capitalize()} beats {computer_choice}"
            self.user_score += 1
        else:
            result = f"You lose! {computer_choice.capitalize()} beats {user_choice}"
            self.computer_score += 1
        
        self.result_label.config(text=f"Your choice: {user_choice.capitalize()}\n"
                                    f"Computer's choice: {computer_choice.capitalize()}\n"
                                    f"{result}")
        
        self.update_scores()
    
    def update_scores(self):
        self.user_score_label.config(text=str(self.user_score))
        self.computer_score_label.config(text=str(self.computer_score))
        self.ties_label.config(text=str(self.ties))
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.update_scores()
        self.result_label.config(text="")
        messagebox.showinfo("Game Reset", "Scores have been reset!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
