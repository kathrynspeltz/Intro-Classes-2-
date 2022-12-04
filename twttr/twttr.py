tweet = input("Input: ")
print("Output: ", end="" )
for i in tweet:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
print("\n")
