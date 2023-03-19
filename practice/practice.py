price = [1, 2, 3]
discount = [.5, .2, .3]

def shopping(a,b):
    bill1 = 0
    for (a, b) in zip(price, discount):
        bill1 += (a * b)
    return(bill1)

print(shopping(price, discount))