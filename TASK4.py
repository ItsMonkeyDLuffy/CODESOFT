'''This project aims to create a Rock-Paper-Scissors Game'''

import random

while True:
    a = input("stone, paper or scissors: ").lower()
    
    if a in ["stone", "paper", "scissors"]:
        b = random.choice(["stone", "paper", "scissors"])
        print("Computer chooses:", b)
        if a == b:
            print("Draw")
        elif (a == "stone" and b == "scissors") or \
            (a == "paper" and b == "stone") or \
            (a == "scissors" and b == "paper"):
            print("User wins")
        else:
            print("Computer wins")
    else:
        print("Invalid choice. Please enter 'stone', 'paper', or 'scissors'.")
        continue

    c = input("Do you want to play again (yes/no): ")
    if c.lower() != "yes":
        print("Thank you for playing")
        break
    
    

    
