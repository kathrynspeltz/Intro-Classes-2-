

def main():
    time = input("what time is it? ")
    new_time = convert(time)

    if "7" <= new_time >= "8":
        print("breakfast time")

    elif "11" <= new_time >= "12":
        print("lunch time")

    elif "18" <= new_time >= "19":
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    float(hours)
    float(minutes)/60
    return(hours + minutes)

main()
