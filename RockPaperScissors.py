"""
A simple game where the user plays Rock, Paper, Scissors against the computer.
Requirements:
- The user selects rock, paper, or scissors
- The computer makes a random choice
- Compare choices and determine the winner
- Allow the user to play multiple rounds
"""
import random

# Computer makes random decision
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
computer_choice = computer_choice.casefold()

# Initialize the loop
run = "y"

while run == "y":
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Type \"rock,\" \"paper,\" or \"scissors\" to start the round.")

    # Get user choice
    user_choice = input("I choose ")
    user_choice = user_choice.casefold()

    # Decide who wins by comparing user and computer choices
    if user_choice == computer_choice:
        # If decisions are the same then tie
        print(f"Computer chooses {computer_choice}.")
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper":
        # If user choose rock and computer chooses paper
        print(f"Computer chooses {computer_choice}.")
        print("You lose! Better luck next time.")
    elif user_choice == "paper" and computer_choice == "scissors":
        # If user choose paper and computer chooses scissors
        print(f"Computer chooses {computer_choice}.")
        print("You lose! Better luck next time.")
    elif user_choice == "scissors" and computer_choice == "rock":
        # If user choose scissors and computer chooses rock
        print(f"Computer chooses {computer_choice}.")
        print("You lose! Better luck next time.")
    elif user_choice == "rock" and computer_choice == "scissors":
        # If user choose rock and computer chooses scissors
        print(f"Computer chooses {computer_choice}.")
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        # If user choose paper and computer chooses rock
        print(f"Computer chooses {computer_choice}.")
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        # If user choose scissors and computer chooses paper
        print(f"Computer chooses {computer_choice}.")
        print("You win!")
    else:
        # If something other than what is allowed is entered by the user
        print("Invalid response. Please enter either \"Rock,\" \"Paper,\" or \"Scissors.\"")
        continue

    # Ask user if they want to play again
    run = input("Play again? Type \"y\" or \"n\" to confirm: ")
else:
    # Quit game
    print("Ending game...")
    quit()