#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("enter side 1:"))
b = int(input("enter side 2:"))
c = int(input("enter side 3:"))

if a == b and b == c:
    print("triangke is equilateral")
elif a==b or b==c or c==a:
    print("triangle is isosceles")
else:
    print("triangle is scalene")


