"""While loop exercises – echo, password, and more."""

# 🔹 Exercise 1: Echo until 'quit'


def exercise1():
    command = ""
    while command != "quit":
        command = input(">")
        print("ECHO", command)

# 🔹 Exercise 2: Password with 3 attempts


def exercise2():
    correct_password = "open123"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted.")
            break
        else:
            attempts += 1
            print(f"Wrong password. Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("Too many attempts. Access denied.")

# 🔹 Exercise 3: Guess the number


def exercise3():
    correct_number = 7
    guess = -1

    while guess != correct_number:
        guess = int(input("Guess a number (1–10): "))
        if guess != correct_number:
            print("Wrong! Try again.")
    print("You got it!")

# 🔹 Exercise 4: Count numbers until 'done'


def exercise4():
    count = 0
    user_input = ""

    while user_input != "done":
        user_input = input("Enter a number or 'done': ")
        if user_input.isdigit():
            count += 1
    print(f"You entered {count} numbers.")

# 🔹 Exercise 5: Help command menu


def exercise5():
    command = ""

    while command != "quit":
        command = input("> ").lower()

        if command == "help":
            print("Available commands: help, hello, quit")
        elif command == "hello":
            print("Hi there!")
        elif command != "quit":
            print("Unknown command.")


# 🔸 SELECT WHICH ONE TO RUN
if __name__ == "__main__":
    # Uncomment ONLY ONE of these to test it:

    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    exercise5()
