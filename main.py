import random

print("Welcome to Rock, Paper, Scissors!")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name: ")

while True:
    print("""
    Winning rules:
    1. Paper vs Rock --> Paper
    2. Rock vs Scissors --> Rock
    3. Scissors vs Paper --> Scissors
    """)

    print("Choices are:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1/2/3): ")

    if user_choice not in ['1', '2', '3']:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue

    user_choice = int(user_choice)
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("Your choice:", choices[user_choice])

    comp_choice = random.randint(1, 3)
    print("Computer's choice:", choices[comp_choice])

    if user_choice == comp_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 2 and comp_choice == 1) or (user_choice == 3 and comp_choice == 2):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print(f"Score - {name}: {user_score} / Computer: {comp_score} / Ties: {ties}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
