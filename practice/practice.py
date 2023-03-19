price = [1, 2, 3]
discount = [.5, .2, .3]


def shopping(list):
    bill1 = 0
    for a, b in list:
        bill1 += (a * b)
    return bill1


print(shopping(price, discount))
