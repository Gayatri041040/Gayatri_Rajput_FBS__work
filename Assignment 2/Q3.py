#Convert distant given in feet and inches into meter and centimeter.
#take input.
feet = float(input("distance in feet:"))
inches = float(input("distance in inches:"))

#perform operation.
total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meter = cm / 100

print("distance in meter =" ,meter)
print("distance in centimeter =" ,cm)