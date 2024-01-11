# Old For loop

numbers = [1, 2, 3, 4, 5]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# New List Comprehension

new_list2 = [n + 1 for n in numbers]

# Doesn't have to be for just lists
name = "Brandon"
letters_name = [n for n in name]
print(letters_name)

# Create range 1-5

doubled = [x * 2 for x in range(1, 6)]
print(doubled)

# additional length to list comprehension

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [(len(x) < 5) for x in names]
short_names2 = [name for name in names if (len(name) < 5)]
print(short_names)
print(short_names2)


