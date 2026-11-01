import random
you = input("Enter your choice (rock, paper, scissors): ").lower()
game = {"rock": 0, "paper": 1, "scissors": 2}
you_choice = game[you]
computer_choice = random.choice([0,1,2])
reverse = {0: "rock", 1: "paper", 2: "scissors"}
print(f"Computer chose: {reverse[computer_choice]} you chose: {you}")
if you_choice == computer_choice:
    print("It's a tie!")
else:
    if (you_choice == 0 and computer_choice == 2) or (you_choice == 1 and computer_choice == 0) or (you_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
