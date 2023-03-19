price = [1, 2, 3]
discount = [.5, .2, .3]

bill1 = 0

for a, b in price, discount:
    bill1 += (a * b)
    print(bill1)

