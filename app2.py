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
