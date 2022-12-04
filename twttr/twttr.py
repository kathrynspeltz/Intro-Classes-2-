Tweet = input("What's your Tweet? ")
print("snakecase: ", end="" )
for i in name:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
print("\n")
