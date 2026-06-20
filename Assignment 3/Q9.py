#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input("enter marks of subject 1:"))
m2 = int(input("enter marks of subject 2:"))
m3 = int(input("enter marks of subject 3:"))
m4 = int(input("enter marks of subject 4:"))
m5 = int(input("enter marks of subject 5:"))

total = m1 + m2 + m3+ m4 + m5
per = total / 5

if per >= 90:
    print("first class.")
elif per >= 70:
    print("second class.")
elif per >= 35:
    print("pass")
else:
    print("fail")
