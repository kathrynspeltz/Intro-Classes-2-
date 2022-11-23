hours, minutes = int(input("what time is it? ")).split(":")

if hours == 7:
    print(breakfast)
if hours == 8 and minutes == 00:
    print(breakfast)

elif hours == 12:
    print(lunch)
elif hours == 13 and minutes == 00:
    print(lunch)

if hours == 18:
    print(breakfast)
if hours == 19 and minutes == 00:
    print(breakfast)