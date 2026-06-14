#program to find the roots of quadratic equation.
#take input
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

#Perform operation
d = b ** 2 - (4 * a *c)

r1 = (- b +(d ** 0.5)) / (2 * a)

r2 = (-b - (d ** 0.5)) / (2* a)

#display result
print("root 1:" ,r1)
print("root 2:" ,r2)
