def multiples(nums):
    value = 0
    for i in nums:
        if i%3 == 0 or i%5 == 0:
            value += i
    return i

print(multiples(10))


