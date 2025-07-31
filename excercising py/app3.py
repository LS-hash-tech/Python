# ============================== While loops challanges ====================================

def exercise1():
    password = "zz"
    while password != "open":
        password = input("enter password please: ")
    print("access granted")


def exercise2():
    correct_password = "open123"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter Password please: ")
        if password == correct_password:
            print("Access Granted")
            break
        print(
            f"wrong password. Attempts left: {max_attempts - attempts}")
        attempts += 1
        if attempts == max_attempts:
            print("too many attempts, access denied")


# ============================== general exercises ====================================
