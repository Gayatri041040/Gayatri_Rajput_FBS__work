#Write a program to calculate area of an equilateral triangle.
# Take input
import math
side = int(input("enter side:"))

#perform operation.
area = (math.sqrt(3) / 4) *(side ** 2)

#Display result.
print('Area =' ,area)