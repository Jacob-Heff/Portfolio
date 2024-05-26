# Jacob Heffington
# Rock, Paper, Scissors
# Resource: github.com/techwithtim/5-Python-Projects-For-Beginners

import random

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")
    
    if user_input == computer_pick:
        print("You tied! Noone wins!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
    
print("Final score:")
print("You Won:", user_wins,"times.")
print("Computer Won:", computer_wins,"times.")
print("Goodbye!")