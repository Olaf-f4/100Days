import random

random_integer = random.randint(1, 5)
print(random_integer)

random_float = random.random()
print(random_float)

print(random_integer + random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}%")


# Coin Toss
tails = 0
heads = 1
coin = random.randint(0, 1)

if coin == tails:
    print("Tails")
else:
    print("Heads")

# Banker Roulette

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
print(names)

num_items = len(names)
random_generate = random.randint(0, num_items -1)

print(names[random_generate])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][2])














# Treasure map - Mine

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
letter = position[0].lower()
# A = Line 1 , B = Line 2 , C = Line 3
#  B3 - 1

if position[1] == "1":
    if position[0] == "a":
        map[0][0] = "X"
    if position[0] == "b":
        map[0][1] = "X"
    if position[0] == "c":
        map[0][2] = "X"
elif position[1] == "2":
    if position[0] == "a":
        map[1][0] = "X"
    if position[0] == "b":
        map[1][1] = "X"
    if position[0] == "c":
        map[1][2] = "X"
else:
    if position[0] == "a":
        map[2][0] = "X"
    if position[0] == "b":
        map[2][1] = "X"
    if position[0] == "c":
        map[2][2] = "X"


print(f"{line1}\n{line2}\n{line3}")


# Treasure map - Hers

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

letter = position[0].lower()  # B3 <- (example)
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")

