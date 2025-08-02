# ======================================== dice roll game ======================================
#
# PERSONAL TEST: functions and structure

# ask: roll the dice? (Y/N)

# answer Y or N
# N = "Thank you for playing and have a great rest of your day" aka end the game
# Y = two random numbers in parenthesis for two dices -- eg. (2, 5) -- each dice can offer from 1 to 6
# Anything else? = Invalid choice!

import random
Y = (1, 2, 3, 4, 5, 6)
N = "Thank you for playing and have a great rest of your day"

for numbers in range(1, 6):
    if Y:
        print("{numbers}")
    elif N:
        print("Thank you for playing and have a great rest of your day")
    else:
        print("Sorry, invalid choice!")

Numbers = (1, 2, 3, 4, 5, 6)

# The outcome for this Personal attempt came out with Numbers x 5

# Attempt 2 (with some inside info!)


choice = input
