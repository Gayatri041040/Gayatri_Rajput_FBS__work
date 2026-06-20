#Write a program to calculate profit or loss.
cp = int(input("Enter cost price:"))
sp = int(input("Enter selling price:"))

if(cp < sp):
    print("profit")
    
elif(cp == sp):
    print("not profit not loss")

else:
    print("loss")


