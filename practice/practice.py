
def old_macdonald(name):
    for i in name:
        if i == 0 or i == 3:
            return i.upper()
        else:
            return i

print(old_macdonald("macdonald"))