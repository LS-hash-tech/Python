
even_number = 0

for number in range(1, 10):
    if number % 2 == 0:
        print(f"{number} even")
        even_number += 1  # means count 1 for every even number
    else:
        print(f"{number} odd")


print(f"we have a total of {even_number} even numbers")

#  % = is the modulo operator (gives you a leftover part after dividing)


# ==================================== Arguments & Parameters =============================

def greet(first_name, second_name):  # the first_name & second_name are parameters (defined by us)
    print(f"hi {first_name} {second_name}")
    print("how are you doing today?")


# The arguments ("Layne", "Singh") are the values given to the parameters
greet("Layne", "Singh")
