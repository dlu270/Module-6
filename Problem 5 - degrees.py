# Daniel Lu
# 9/12/20

# This program converts radians to degrees, it prints an approximation as well as the calculated value.

import math

radians = int(input("What is the number of radians?: "))
degrees = radians*(180/3.141)
print ("Approximate degrees =", degrees)

degrees_calc = math.degrees(radians)
print ("Calculated degrees =", degrees_calc)