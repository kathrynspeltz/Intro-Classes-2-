print("Amount Due: 50")
value = int(input("Insert Coin: "))

cost = 50
added = 0


if value == 25 or value == 10 or value == 5:
    added += value
    while added < 50:
        print("Amount Due: ", cost - added)
        break

else:
        print("Amount Due: ", cost - added)
        break

if added > 50:
    print("Change Owed: ", (added - 50))