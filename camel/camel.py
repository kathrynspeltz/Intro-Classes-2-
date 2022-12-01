name = input("camelcase: ")

for i in name:
    if i.islower():
        print(i)
    else:
        print("_" + i.lower())









