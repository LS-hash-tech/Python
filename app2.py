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
