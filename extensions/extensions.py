response = input("what is your file name? ").casefold().strip()

if response.endswith(".gif"):
    print("image/gif")
elif response.endswith(".jpg") or esponse.endswith(".jpeg"):
    print("image/jpeg")
elif response.endswith(".png"):
    print("image/png")
elif response.endswith(".pdf"):
    print("application/pdf")
elif response.endswith(".txt"):
    print("text/plain")
elif response.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")