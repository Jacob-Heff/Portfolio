# Jacob Heffington
# Number Guesser
# Resource: github.com/techwithtim/5-Python-Projects-For-Beginners

import random

def game(limit, guesses, guessed):
    rng = random.randint(1, limit)

    while guessed == 0:
        guess = int(input("Your guess: "))
        if guess == rng:
            guessed = 1
        elif guess < rng:
            print ("Too low.")
        elif guess > rng:
            print ("Too high.")
        guesses += 1
        
    print("You guessed it in " + str(guesses) + " tries.\n")

print ("Guess the number!")
print ("")    
    
run = 1
while run == 1:
    limit = int(input("Enter the limit: "))
    print ("I'm thinking of a number from 1 to " + str(limit))
    print ("")
    
    game(limit, guessed = 0, guesses = 0)
    replay = input("Would you like to play again? (y/n): ")
    print("")
    if replay == "n":
        print("Bye!")
        run = 0