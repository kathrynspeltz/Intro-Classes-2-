tweet = input("Input: ")
print("Output: ", end="" )
for c in tweet:
    if c.re.search("[a , e , i , o , u]"):
        print(c, end="")
    else:
        print("", end="")
print("\n")
