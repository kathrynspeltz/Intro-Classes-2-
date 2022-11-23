

def main():
    time = input("what time is it? ")

    if hours == "7":
        print("breakfast time")
    elif hours == "8" and minutes == "0":
        print("breakfast time")

    elif hours == "12":
        print("lunch time")
    elif hours == "13" and minutes == "0":
        print("lunch time")

    elif hours == "18":
        print("dinner time")
    elif hours == "19" and minutes == "0":
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    float(hours)
    float(minutes)/60
