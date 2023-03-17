

def animal_crackers(animal):
    wordlist = animal.split()
    if wordlist [0][0] == wordlist [1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded zlama'))