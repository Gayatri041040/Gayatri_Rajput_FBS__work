#Find the sum of three-digit number.
#Take input.
num = int(input("Enter a three digit number:"))

#perform operation.
a = num // 100
b = (num // 10) % 10
c = num % 10

sum_digit = a + b + c

#display result
print("sum of digits =" ,sum_digit)
