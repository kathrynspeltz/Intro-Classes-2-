

def main():
    time = convert(input("what time is it? "))

    if "7" <= time >= "8":
        print("breakfast time")

    elif "11" <= time >= "12":
        print("lunch time")

    elif "18" <= time >= "19":
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    float(hours)
    float(minutes)/60
