
# ==================================== Types of functions =============================

def greet(name):
    print(f"hi {name}")

    # 1. words after "def greet" are used to perform a task
    # 2. meanwhile print is to return a value


def get_greeting(name):
    return f"hii {name}"


message = get_greeting("Layne")
print(message)

# ==================================== keyword arguments ===============================


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# below a shortened version that hides the variable


def increasee(number, by):
    return number + by


# you can make your code me readable by adding the variables and a = sign
print(increasee(number=2, by=1))

# ==================================== default value ====================================


def increase(number, by=1):  # you can add the same "variabe =" sign at the beginning and the outcome won't change
    return number + by


print(increase(number=2))

# ==================================== xargs ====================================


def multiply(x, y):
    return x * y


multiply(2, 3)

# we can utilise "Tuples" see below


# because we changed the variables into the plural form of number...
def multiply1(*numbers):
    print(numbers)


multiply1(2, 3, 4, 5, 6, 7, 8)  # ...we can now add as many numbers as we like

# we can also utilise "Tuples" within a "loop" see below


def multiply2(*numbers):
    total = 1  # 1 is how many times the loops gets run
    for numbers in numbers:
        total *= numbers
    return total  # we must move the "return" behind by one column to not be part of the "for" loop!


print(multiply2(2, 3, 4, 5))
