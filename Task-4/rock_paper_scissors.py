import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    global user_score, computer_score, ties
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
        ties += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = f"You win! {user_choice} beats {computer_choice}"
        user_score += 1
    else:
        result = f"You lose! {computer_choice} beats {user_choice}"
        computer_score += 1
    
    result_label.config(text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}")
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}  Ties: {ties}")

def reset_game():
    global user_score, computer_score, ties
    user_score = 0
    computer_score = 0
    ties = 0
    result_label.config(text="")
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}  Ties: {ties}")
    messagebox.showinfo("Game Reset", "Scores have been reset!")

user_score = 0
computer_score = 0
ties = 0

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x400")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 12))
instruction_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=8, command=lambda: play_game("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=8, command=lambda: play_game("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=8, command=lambda: play_game("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"You: {user_score}  Computer: {computer_score}  Ties: {ties}", font=("Arial", 12))
score_label.pack()

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
