
price = [2, 4, 6, 8]
discount = [.2, .4, .6, .8]

def groceries(a, b):
    bill1 = 0
    for (a, b) in zip(price, discount):
        bill1 += (a * b)
    if bill1 > 20:
        return "cannot afford"
    if bill1 <= 20:
        return "good to go"

print(groceries(price,discount))