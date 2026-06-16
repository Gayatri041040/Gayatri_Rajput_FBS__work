#Write a program to reverse three-digit number.
#Take input
num =int(input("Enter the number:"))

#perform operation.
hundreads = num // 100  
tens = (num // 10) % 10
units = num % 10

reverse = units * 100 + tens * 10 + hundreads

#display result.
print("Reverse number =" ,reverse)

