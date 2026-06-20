#Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter any alphabet:")
vowel = ['a' ,'e' ,'i' ,'o' ,'u']

if alphabet in vowel:
    print("this is vowel.")
else:
    print("this is consonant.")
