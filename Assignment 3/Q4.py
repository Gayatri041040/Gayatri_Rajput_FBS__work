#Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("enter third side:"))
 
if(a+b>c and a+c>b and b+c>a):
    print("triangle is valid.")
else:
    print("triangle is not valid.")


