#write a program to enter p t r and calculate compound intererest
#Take input.
p = float(input("enter princial amount:"))
r = float(input("enter rate interest:"))
t = float(input("enter time:"))

#perform operation.
amount = p*(1 + r/100) **t
ci =amount-p

#Display result.
print("ci =" ,ci)