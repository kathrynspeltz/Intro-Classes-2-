hours, minutes = input("what time is it? ")

def main():
    ...


def convert(time):
    ...hours, minutes = time.split(":")


if __name__ == "__main__":
    main()



hours, minutes = input("what time is it? ")

if hours == "7":
    print("breakfast time")
elif hours == "8" and minutes == "00":
    print("breakfast time")

elif hours == "12":
    print("lunch time")
elif hours == "13" and minutes == "00":
    print("lunch time")

elif hours == "18":
    print("dinner time")
elif hours == "19" and minutes == "00":
    print("dinner time")