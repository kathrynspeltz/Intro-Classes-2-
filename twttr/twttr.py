tweet = input("Input: ")
print("Output: ", end="" )
vowels = ["a" , "e" , "i" , "o" , "u", "A" , "E" , "I" , "O" , "U"]
for c in tweet:
    if c in vowels:
        print("", end="")
    else:
        print(c, end="")
print("\n")
