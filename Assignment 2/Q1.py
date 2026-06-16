#Convert the time entered in hh,min and sec into seconds.
hr = int(input("enter hours:"))
min = int(input("enter minute:"))
sec = int(input("enter second:"))

sec = (hr * 3600) + (min * 60) + sec

print("total seconds =" ,sec)