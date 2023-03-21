
lista = [2, 4, 6, 8]

def show_even_indices(nums):
    listb = []
    for i in nums:
        if i % 2 == 0:
            listb.append(lista.index(i))
    return listb

print(show_even_indices(lista))