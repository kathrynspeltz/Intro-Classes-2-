
def vowels(words):
    newlist = ""
    for n in words:
        if n[0] == "i" or n[0] == "e" or n[0] == "o" or n[0] == "u":
            newlist.append(n)
    return newlist

print(vowels(["elephant", "hello", "octopus"]))
