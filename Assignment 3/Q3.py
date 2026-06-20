#Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input("enter a first angle of triangle:"))
b = int(input("enter a second angle of triangle:"))
c = int(input("enter a third angle of triangle:"))

triangle = a + b + c 

if(a + b + c == 180):
    print("triangle is valid.")
else:
    print("triangle is not valid.")

