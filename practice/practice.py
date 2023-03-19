price = [2, 5, 7]
discount = [.5, .2, .3]

def shopping(c,d):
    bill1 = 0
    for (a, b) in zip(c,d):
        bill1 += (a * b)
    if bill1 > 20:
        return "cannot afford"
    else:
        return "good to go"

print(shopping(price, discount))