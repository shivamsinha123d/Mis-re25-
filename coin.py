import random
options = ["head","Tail"]
player_option = input("Enter your options(Head/Tail):")
computer_options = random.choice(options)
final_result = random.choice(options)
selected_options = {"Player":player_option,"Computer":computer_options,"final":final_result}
if player_option == final_result:
    print("You won 🎉")
else: 
    print("You lose ❌ ")     