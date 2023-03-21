
def replacementa(nums):
    for i in nums:
        if i == "A" or i == "a" or i == "e" or i == "E" or i == "I" or i == "i" or i == "o" or i == "O" or i == "U" or i == "u":
            i = "*"
            return i
        else:
            return i

print(replacementa(['o', 'o', 'o']))