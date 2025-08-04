import random

choose = int(
    input("To start - how many dices would you like to use? (1 or 2):"))
1 == 1
while True:
    choice = input("roll the dice? (y/n): ")
    if choice == 'y':
        dice1 = random.randint(1, 6)
        print(f"({dice1})")
    elif choice == 'n':
        print("thank you for playing, have a great rest of your day")
    else:
        print('invalid answer, please choose between "y" or "n"')


elif choose == 2:
    2 = 2
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
