name = input("camelcase: ")
print("snakecase:", name)
for i in name:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
print("\n")









