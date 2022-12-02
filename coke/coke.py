print("Amount Due: 50")


cost = 50
added = 0

while added <= 50:
    value = int(input("Insert Coin: "))
    if value == 25 or value == 10 or value == 5:
            added += value
            if added >= 50:
                print("Change Owed: ", (added - 50))
                break
            else:
                print("Amount Due: ", 50 - added)
    else:
        print("Amount Due: ", 50 - added)
