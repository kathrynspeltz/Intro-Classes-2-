
list2 = [2, 4, 6, 8]

def show_even_indices(nums):
    lista = []
    for i in nums:
        if i % 2 == 0:
            lista += i
    return lista

print(show_even_indices(list2))