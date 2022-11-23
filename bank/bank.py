response = input("How would you like to be greeted? ").casefold().strip()

if response == "hello":
    print("$0")
elif response.startswith("h"):
    print("$20")
else:
    print("$100")