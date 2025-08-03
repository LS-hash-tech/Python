
import random

while True:
    choice = input("roll the dice? (y/n): ")
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif choice == 'n':
        print("thank you for playing, have a great rest of your day")
    else:
        print('invalid answer, please choose between "y" or "n"')
