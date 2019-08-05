import random

print("Welcome to Dice simulator")
user_input = input("Roll the dice: [Y/N] ")
if user_input == 'Y' or user_input == 'y':
    print(random.randint(1, 7))
else:
    print("break")
