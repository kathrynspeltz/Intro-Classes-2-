response = input("what is your file name? ").casefold().strip()

if response.endswith(".gif"):
    print("image/gif")
if response.endswith(".jpg"):
    print("image/jpeg")
if response.endswith(".jpeg"):
    print("image/jpeg")