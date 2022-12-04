tweet = input("Input: ")
print("Output: ", end="" )
vowels = ["a" , "e" , "i" , "o" , "u"]
for c in tweet:
    if c.search(vowles):
        print(c, end="")
    else:
        print("", end="")
print("\n")
