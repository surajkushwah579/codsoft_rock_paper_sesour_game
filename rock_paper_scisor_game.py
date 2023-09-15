import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It is a tie "
    if (user_choice=='rock' and computer_choice=='scissors')or\
       (user_choice=='scissors' and computer_choice=='paper')or\
       (user_choice=='paper' and computer_choice=='rock'):
        return "you win"
    return "computer wins"

def play_game(user_choice):
    computer_choice=['rock','paper','scissors']
    computer_choice=random.choice(computer_choice)
    
    result=determine_winner(user_choice,computer_choice)

    message=f"You chose: {user_choice}\n Computer chose: {computer_choice}\n\nResult: {result}"
    messagebox.showinfo("Game Result", message)

def on_rock_click():
    play_game("rock")
def on_paper_click():
    play_game("paper")
def on_scissors_click():
    play_game("scissors")

root=tk.Tk()
root.title("Rock.Paper-Scissors Game")


rock_button=tk.Button(root,text="Rock",command=on_rock_click)
paper_button=tk.Button(root,text="Paper",command=on_paper_click)
scissor_button=tk.Button(root,text="Scissor",command=on_scissors_click)

rock_button.pack(pady=50)
paper_button.pack(pady=50)
scissor_button.pack(pady=50)

play_again=input("play again")
if not play_game=="y":
   running=False
root.mainloop()
print("Thanks for playing")

     