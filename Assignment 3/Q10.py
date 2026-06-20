#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('enter gender (m/f):')

age = int(input('enter age:'))

if(gender == 'f'):
    if(age >= 18):
        print('girl is eligible fr marriage.')
    else:
        print('pahele bade h jao.')
else:
    if(age >= 21):
        print('boy is eligible for marriagge')
    else:
        print('kama lo pahele')
