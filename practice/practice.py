
def old_macdonald(name):
    name2 = name.split()
    for i in name2:
        if i == 0 or i == 3:
            print(i.upper())
        else:
            print(i)

print(old_macdonald("macdonald farm"))