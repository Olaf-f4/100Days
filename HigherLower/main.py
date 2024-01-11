from art import logo
from art import vs
from game_data import data
import random

print("Welcome to higher or lower")


def generate(last):
    if last == {}:
        selection = random.choice(data)
        selection2 = random.choice(data)

        # check if selection is already selected
        if selection2["name"] == selection["name"]:
            selection2 = random.choice(data)

        return selection, selection2
    else:
        selection = last
        selection2 = random.choice(data)

        if selection2["name"] == selection["name"]:
            selection2 = random.choice(data)

        return selection, selection2


def logic(selection, selection2):
    a_count = int(selection["follower_count"])
    b_count = int(selection["follower_count"])
    correct = ""
    actor = ()

    if a_count > b_count:
        correct = "a"
        actor += selection
    else:
        correct = "b"
        actor += selection2

    check = input("Who has more followers? Type 'A' or 'B': ").lower()

    print(type(actor))

    if check == correct:
        return actor
    else:
        return actor


tries = 5
actor = {}
while tries > 0:
    print(logo)
    comparison = generate(actor)
    print(f"Compare A: {comparison[0]["name"]}, a {comparison[0]["description"]} "
          f"from {comparison[0]["country"]}.")
    print(vs)
    print(f"Against B: {comparison[1]["name"]}, a {comparison[1]["description"]} "
          f"from {comparison[1]["country"]}.")

    logic = logic(comparison[0], comparison[1])

    if not logic:
        tries -= 1
    else:
        actor = logic





