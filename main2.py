# Creating a 21 Number Game
import random
import time

print("------Welcome to 21 Number Game 🎮------\n")
time.sleep(1)

# Rules
print("-------------< Rules of the Game >-------------")
print("| Rule No.1 : Pick 1, 2, or 3 numbers per turn |")
print("| Rule No.2 : The player who gets 21 wins      |")
print("-----------------------------------------------\n")
time.sleep(1)

option_to_continue = input("-- Do you wish to continue❓(Yes/No)-- \n")
print()

if option_to_continue.lower() == "yes":
    print("First we will play a coin toss 🪙 to decide who will start the game first")
    time.sleep(1)
    print("Welcome to the game 🎮")
    print("Head or Tail? 🪙")

    options = ["Head", "Tail"]
    player_option = input("Enter your option (Head/Tail): ").capitalize()
    computer_options = random.choice(options)
    final_result = random.choice(options)
    selected_options = {"Player": player_option, "Computer": computer_options, "final": final_result}
    print(f"Coin shows: {final_result}\n")

    if player_option == final_result:
        time.sleep(0.75)
        print("You won 🎉")
        start = True
    else:
        time.sleep(0.75)
        print("You lose ❌")
        start = False

    time.sleep(1)
    total = 0
    print("Let's start the 21 Number Game 🎮\n")
    time.sleep(1)

    if start:
        print("👉 You will start first\n")
    else:
        print("👉 Computer will start first\n")

    while total < 21:
        if start:
            # Player turn
            player_choice = int(input("Enter your choice (1,2,3): "))
            if player_choice not in [1, 2, 3] or total + player_choice > 21:
                print(f"Invalid choice! You cannot exceed 21. Current total: {total}\n")
                continue
            total += player_choice
            print(f"Total is {total}\n")
            if total == 21:
                print("You reached 21 🎉 You win!")
                break

            # Computer turn
            computer_choice = random.randint(1, 3)
            while total + computer_choice > 21:
                computer_choice = random.randint(1, 3)
            total += computer_choice
            print(f"Computer chose {computer_choice}")
            print(f"Total is {total}\n")
            if total == 21:
                print("Computer reached 21 🎉 Computer wins!")
                break

        else:
            # Computer turn
            computer_choice = random.randint(1, 3)
            while total + computer_choice > 21:
                computer_choice = random.randint(1, 3)
            total += computer_choice
            print(f"Computer chose {computer_choice}")
            print(f"Total is {total}\n")
            if total == 21:
                print("Computer reached 21 🎉 Computer wins!")
                break

            # Player turn
            player_choice = int(input("Enter your choice (1,2,3): "))
            if player_choice not in [1, 2, 3] or total + player_choice > 21:
                print(f"Invalid choice! You cannot exceed 21. Current total: {total}\n")
                continue
            total += player_choice
            print(f"Total is {total}\n")
            if total == 21:
                print("You reached 21 🎉 You win!")
                break

else:
    print("\nThank you for visiting! Goodbye 👋")
