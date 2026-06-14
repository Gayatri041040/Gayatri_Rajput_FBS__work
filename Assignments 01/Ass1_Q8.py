#write a program to convert days into years weeks into days.
#take input
days = int(input("entr days:"))

years = days // 365
days =days % 365

weeks = days // 7
days = days % 7

print(f'YEARS:{years} , WEEKS:{weeks} , DAYS:{days}')