response = input("what is your file name? ").casefold().strip()

if response.endswith(".gif"):
    print("image/gif")
if response.endswith(".jpg"):
    print("image/jpeg")
if response.endswith(".jpeg"):
    print("image/jpeg")
if response.endswith(".png"):
    print("image/png")
 if response.endswith(".pdf"):
    print("application/pdf")
if response.endswith(".txt"):
    print("text/plain")
if response.endswith(".zip"):
    print("application/zip")