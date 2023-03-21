
lista = [2, 4, 6, 8, 11, 3, 6]

def oddeven(nums):
    listeven = []
    listodd = []
    for i in nums:
        if i%2 == 0:
            listeven.append(i)
        else:
            listodd.append(i)
    if len(listeven) > len(listodd):
        return "Even"
    elif len(listeven) < len(listodd):
        return "Odd"

print(oddeven(lista))