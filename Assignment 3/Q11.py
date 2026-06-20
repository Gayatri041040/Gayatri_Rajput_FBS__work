#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total = 0
age = int(input("Enetr age 1:"))
ticket = int(input("Enter ticket amount:"))
if age < 12:
    total = total + (ticket - ticket*30/100)
elif age > 59:
    total = total + (ticket - ticket * 50 / 100)
else:
    total = total + ticket 

age = int(input("Enetr age 2:"))
ticket = int(input("Enter ticket amount:"))
if age < 12:
    total = total + (ticket - ticket * 30 / 100)
elif age > 59:
    total = total + (ticket -ticket * 50 / 100)
else:
    total = total + ticket 

age = int(input("Enetr age 3:"))
ticket = int(input("Enter ticket amount:"))
if age < 12:
    total = total + (ticket - ticket * 30 / 100)
elif age > 59:
    total = total + (ticket - ticket * 50 / 100)
else:
    total = total + ticket 

age = int(input("Enetr age 4:"))
ticket = int(input("Enter ticket amount:"))
if age < 12:
    total = total + (ticket - ticket * 30 / 100)
elif age > 59:
    total = total + (ticket - ticket * 50 / 100)
else:
    total = total + ticket 

age = int(input("Enetr age 5:"))
ticket = int(input("Enter ticket amount:"))
if age < 12:
    total = total + (ticket - ticket * 30 / 100)
elif age > 59:
    total = total + (ticket -ticket * 50 / 100)
else:
    total = total + ticket 

print("total amount =" ,total)
