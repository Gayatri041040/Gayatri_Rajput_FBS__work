#Write a program to check if the given number is positive or negative.
num = int(input("enter a number:"))

if(num > 0):
    print(f"{num} is the positive number.")

elif(num < 0):
    print(f"{num} is the negative number.")

else:
    print(f"{num} is zero.")


