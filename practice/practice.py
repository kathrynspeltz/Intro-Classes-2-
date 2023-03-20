def multiples(nums):
    value = 0
    for i in range(nums):
        if i%3 == 0 or i%5 == 0:
            value += i
    return value

print(multiples(10))


