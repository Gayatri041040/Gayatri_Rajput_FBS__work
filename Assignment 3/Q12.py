#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter the number:"))
 
a = num // 100
c = num % 10

if a == c:
    print("this is palindrome number")
else:
    print("This is not palindrome number")
