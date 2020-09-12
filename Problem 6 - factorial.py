# Daniel Lu
# 9/12/20

# This program calculates the factorial of an input, prints a calculated and function value.

import math

number = int(input("What numbers' factorial would you like to calculate?: "))
factorial = 1

for i in range (1, number+1):
    factorial = factorial * i
print ("Calculated factorial = ", factorial)

factorial_func = math.factorial(number)
print ("Function factorial =", factorial_func)