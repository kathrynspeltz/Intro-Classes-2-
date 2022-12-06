food = input("Item: ")
nutrition = {"apple": 130, "avacado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew": 50,
    "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50,
    "plums": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80}


for fruit in nutrition.values():
    if fruit == food:
        calories = dictionary[fruit]
    print("Calories:", calories)



    dictionary = {'george' : 16, 'amber' : 19}
search_age = raw_input("Provide age")
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print name