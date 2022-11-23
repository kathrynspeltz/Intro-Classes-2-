answer = input("What is the The Answer to the Great Question? ").casefold().strip()
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("yes")
else:
    print("no")
