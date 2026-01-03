import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")
else:
    print("You Lose!")
