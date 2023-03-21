
def show_even_indices(nums):
    lista = []
    for i in nums:
        if nums[i] % 2 == 0:
            lista.append(i)

    return lista

print(show_even_indices([2, 4, 6, 8]))