# Import modules
import tkinter as tk
import random

# Define choices
choices = ["Rock", "Paper", "Scissors"]

# Define rules
rules = {
    "Rock": {"Rock": "Draw", "Paper": "Lose", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Lose"},
    "Scissors": {"Rock": "Lose", "Paper": "Win", "Scissors": "Draw"}
}

# Define score variables
user_score = 0
computer_score = 0

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("300x200")

# Create labels
user_label = tk.Label(window, text="User: 0")
user_label.pack()
computer_label = tk.Label(window, text="Computer: 0")
computer_label.pack()
result_label = tk.Label(window, text="")
result_label.pack()

# Define functions
def play(choice):
    global user_score, computer_score # Access global variables
    user_choice = choice # Get user choice from button
    computer_choice = random.choice(choices) # Get random computer choice
    result = rules[user_choice][computer_choice] # Get result from rules dictionary
    
    # Update score and result labels based on result
    if result == "Win":
        user_score += 1 # Increment user score by 1
        user_label.config(text=f"User: {user_score}") # Update user label with new score
        result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. You win!") # Update result label with win message
        
    elif result == "Lose":
        computer_score += 1 # Increment computer score by 1 
        computer_label.config(text=f"Computer: {computer_score}") # Update computer label with new score 
        result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. You lose!") # Update result label with lose message
        
    else:
        result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. It's a draw!") # Update result label with draw message

# Create buttons for each choice and bind them to play function with corresponding argument        
rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"))
rock_button.pack()
paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"))
paper_button.pack()
scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack()

# Run main loop of window 
window.mainloop()
