#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143

def fibonacci(nums):
    num1 = []
    for i in nums:
        if i%2 == 0:
            num1 += i
    return num1[-1]


print(fibonacci(600851475143))

