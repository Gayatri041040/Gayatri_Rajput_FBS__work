#Write a program to swap two numbers using third variable.
#Take input
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

#perform operatin.
temp = a
a = b
b = temp

#display result
print("after swapping:")
print("first nuumber =" ,a)
print("secnd number =" ,b)
