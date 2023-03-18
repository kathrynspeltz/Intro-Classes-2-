
lista = [1, 3, 3]

def has_33(listb):
    for i in listb:
        if i == 3 and i[i + 1] == 3:
            return True

print(has_33(lista))
