#Write a program to swap two numbers without using third variable.
#Take input
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

#Perform operation.
a = a + b
b = a - b
a = a - b

#Display result.
print("After swapping:")
print("Enter first number =" ,a)
print("Enter second number =" ,b)
