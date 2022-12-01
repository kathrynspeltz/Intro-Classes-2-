name = input("camelcase: ")
print()
for i in name:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
print("\n")









