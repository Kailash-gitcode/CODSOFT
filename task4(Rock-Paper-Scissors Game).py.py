import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors Game")
        master.geometry("400x550")
        master.configure(bg='lightblue')

        # Choices list as class attribute
        self.choices = ['Rock', 'Paper', 'Scissors']

        # Score tracking
        self.user_score = 0
        self.computer_score = 0

        # Title
        self.title_label = tk.Label(master, text="Rock Paper Scissors Game", 
                                    font=("Arial", 16, "bold"), 
                                    bg='lightblue')
        self.title_label.pack(pady=20)

        # Instruction Label
        self.instruction_label = tk.Label(master, 
                                          text="Choose your move:", 
                                          font=("Arial", 12),
                                          bg='lightblue')
        self.instruction_label.pack(pady=10)

        # Button Frame for choices
        self.button_frame = tk.Frame(master, bg='lightblue')
        self.button_frame.pack(pady=10)

        # Choice Buttons
        self.buttons = {}
        for choice in self.choices:
            self.buttons[choice] = tk.Button(self.button_frame, 
                                             text=choice, 
                                             command=lambda c=choice: self.play_game(c),
                                             width=10,
                                             font=("Arial", 12))
            self.buttons[choice].pack(side=tk.LEFT, padx=5)

        # Result Display
        self.result_label = tk.Label(master, 
                                     text="", 
                                     font=("Arial", 12),
                                     bg='lightblue')
        self.result_label.pack(pady=10)

        # Score Display
        self.score_label = tk.Label(master, 
                                    text="Score: You 0 - 0 Computer", 
                                    font=("Arial", 12),
                                    bg='lightblue')
        self.score_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(master, text="Reset Scores", 
                                      command=self.reset_game,
                                      font=("Arial", 12))
        self.reset_button.pack(pady=10)

        # Exit Button (using destroy for guaranteed close)
        self.exit_button = tk.Button(master, text="Exit", 
                                     command=master.destroy,
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10)

    def play_game(self, user_choice):
        # Computer's random choice
        computer_choice = random.choice(self.choices)

        # Determine winner
        result = self.determine_winner(user_choice, computer_choice)

        # Update scores and set result colour
        if result == "You Win!":
            self.user_score += 1
            result_colour = 'green'
        elif result == "Computer Wins!":
            self.computer_score += 1
            result_colour = 'red'
        else:
            result_colour = 'black'

        # Display result
        result_text = (f"You chose {user_choice}\n"
                       f"Computer chose {computer_choice}\n"
                       f"{result}")
        self.result_label.config(text=result_text, fg=result_colour)

        # Update score label
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

        # Ask user if they want to play again
        play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if not play_again:
            self.master.destroy()  # Exit the game if user chooses 'No'

    def determine_winner(self, user_choice, computer_choice):
        # Game logic
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        winning_combos = {
            'Rock': 'Scissors',
            'Scissors': 'Paper',
            'Paper': 'Rock'
        }

        if winning_combos[user_choice] == computer_choice:
            return "You Win!"
        else:
            return "Computer Wins!"

    def reset_game(self):
        # Reset scores and labels
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You 0 - 0 Computer")
        self.result_label.config(text="", fg='black')

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
