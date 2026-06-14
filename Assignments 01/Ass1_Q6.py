#Write a Program to input two angles from user and find third angle of the triangle.
#Take input
a1 = int(input("enetr a first angle:"))
a2 = int(input("enter a second angle:"))
 
#Perform operation.
a3 = 180 - (a1 + a2)

#Display result.
print("third angle =" ,a3)
