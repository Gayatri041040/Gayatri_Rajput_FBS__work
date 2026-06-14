##write a program calculate the percentage of student based n marks in any 5 subjects.
#Take input
m1 = int(input('enter a subject marks:'))
m2 = int(input('enter a subject marks:'))
m3 = int(input('enter a subject marks:'))
m4 = int(input('enter a subject marks:'))
m5 = int(input('enter a subject marks:'))

#perform operation.
total = m1 +m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print('total marks =' ,total )
print('percentage =', percentage)
 
