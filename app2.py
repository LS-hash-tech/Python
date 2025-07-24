import math
first = "Layne"
last = "Singh"
full = f"{len(first)} {2+2+2+2+2+2}"
print(full)

course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.lstrip())
print(course.find("pro"))
print(course.replace("o", "zzzzz"))

# Numbers + engineering
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # double slashes = round it
print(10 ** 3)  # to the power of
x = 10
x = x + 3
x += 3  # same as above but shorter

# exercise N1: MRR grew £2,000 to £18,000 in 12 months, calculate the CMGR.
initial = 2000
final = 18000
months = 12

# Calculate CMGR
# Step-by-step:
# 1. Calculate the ratio: final / initial = 18000 / 2000 = 9
# 2. Raise that to the power of (1 / months) = 1/12 ≈ 0.083
# 3. Subtract 1 to get the monthly growth rate
cmgr = math.pow(final / initial, 1 / months) - 1
print(f"Compound Monthly Growth Rate: {cmgr * 100:.2f}%")

# startup valued at £5 million. You’re growing at a consistent monthly rate of 8%.
# How many months will it take for your valuation to double?

val_initial = 5000000
val_final = 10000000
Monthly_growth = 8  # as it is a percent you need to divide by 100

print(Monthly_growth / 100 + 1)
# valuation is growing by 8% means monthly is growing 108%
# Means each month, the new value is 108% of the previous one
Monthly_growth = 1.08

value = 5000000
growth_rate = 0.08
value *= (1 + growth_rate)  # Same as value *= 1.08

print(5000000 * 1.08)  # M1 = 5400000
print(5400000 * 1.08)  # M2 = 5832000
print(5832000 * 1.08)  # M3 = 6298560
print(6298560 * 1.08)  # M4 = 6802444.800000001
print(6802444.800000001 * 1.08)  # M5 = 7346640.3840000015
print(7346640.3840000015 * 1.08)  # M6 = 7934371.61
print(7934371.61 * 1.08)  # M7 = 8569121.33
print(8569121.33 * 1.08)  # M8 = 9254651.0364
print(9254651.0364 * 1.08)  # M9 = 9995023.11
print(round(9995023.11))

print(f"\nIt took {9} months to double the valuation.")  # M9 = 9995023.11

#  50,000 users. Each month, 12% of users churn (leave the platform).
# How many users will you have after 18 months?

users_initial = 50000
decline_percent = 12
print(decline_percent / 100)  # 0.12
retention_rate = 0.88
months = 18
users_remaining = 50000

# calculate compound monthly churn
# 1 through 18
# y = x + 1
# built in functions:
# int(x)
# float(x)
# bool(x)
# str(x)

Temperature = 15
if Temperature > 30:
    print("it's warm")
    print("You can drink the water!")
elif Temperature > 20:
    print("it's alright")
    print("Thanks, will do")
else:
    print("it's cold")
print("done")

# method 1 of running the below
age = 22
if age >= 18:  # >= equal to greater than or equal to (eg. age restriction)
    print("eligible")
else:
    print("not eligible")

# method 2 of running it (cleaner version also known as ternary operator)
age = 18
message = "eligible" if age >= 18 else "not eligible"
print(message)

# =========================== logical operators ===============================

# and
# or
# not

# use case below

high_income = True
good_credit = True
home_owner = False

if high_income and good_credit:
    print("eligible")
if home_owner is False:
    print("not eligible")

# 2nd use case (self scripted)

working_keyboard = True
Clean_exterior = False
Intact_pixel = True
functioning_speakers = False

if working_keyboard and Intact_pixel and functioning_speakers is True:
    print("eligible")
else:
    print("not eligible")

# 3rd use case (self scripted)

student_id = True
Uniform = False

if student_id or Uniform is not True:
    print("Not eligible to enter in class")
else:
    print("welcome to the lecture")

# 4th use case (self scripted)

new_skateboard = True
new_wheels = False
dented_front = True

if not dented_front:
    print("open for negotiation")
else:
    print("not interested")

# 2nd eg of 4th use
if (dented_front or new_wheels) and not new_skateboard:
    print("open for negotiation")
else:
    print("not interested")

# ======================== chaining comparison operator =========================

age = 67

if age >= 65 and age < 120:
    print("age not suitable")
else:
    print("age suitable")

# the same can be written neater (as per below)

age = 67

if 65 <= age < 120:
    print("not suitable x 2")
else:
    print("age is suiable x 2")

# ================================== Loops ====================================

# loops are great if you want to repeat a process over and over again

for number in range(10):
    print("attempt", number)

# 2nd use case

for number in range(10):
    print("attempt", number + 1, (number + 1) * ".")

    # the outcome is the following:
    # attempt 1 .
    # attempt 2 ..
    # attempt 3 ...
    # and so on................

# code simplification

for number in range(1, 10):  # <---- same result but cleaner code
    print("attempt", number, (number) * ".")

# or

for number in range(1, 10, 2):  # last number means "skip by 2 until 10 is reached"
    print("attempt", number, (number) * ".")

# Use case (self scripted)

for number in range(200, 299, 11):
    # * is used to keep number & dots aligned
    print("shot number", number, (number) * ".")

# ================================== For.. Else ====================================

successful = True

for number in range(1, 100):
    print("Email attempted")
    if successful:
        print("sucessful")
        break  # this will stop lines from being executed 100 times

# what if the attempt was failed and we want to show a different message now?

successful = False

for number in range(1, 100):
    print("Email attempted")
    if successful:
        print("sucessful")
        break
else:    # executed if the loop doesn't reach "break" but runs 100 times
    print("attempted 100 times and failed")
    # eg:
    # Email attempted
    # Email attempted
    # and so on for another 98 times......

# ================================= Nested Loops ==================================

# Essentially one loop inside another loop

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Check personal notes for full breakdown
