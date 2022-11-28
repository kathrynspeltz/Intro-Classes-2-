

def main():
    time = input("what time is it? ")
    new_time = convert(time)

    if 7 <= new_time <= 8:
        print("breakfast time")

    elif 11 <= new_time <= 12:
        print("lunch time")

    elif 18 <= new_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    converted_minute = float(minutes) / 60
    return float(hours) + converted_minute

if __name__ == "__main__":
    main()