import random

# Rock
Rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

# Paper
Paper = '''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

# Scissors
Scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
signs = [Rock, Paper, Scissors]
signs2 = ["Rock", "Paper", "Scissors"]

if player >= 3 or player < 0:
    print("You typed an invalid number, you lose!")
    exit()

print(f"Player chose: \n{signs2[player]}")
print(signs[player])

print("Computer chose:")


Computer = random.randint(0, 2)
print(signs2[Computer])
print(signs[Computer])

player_score = 0
computer_score = 0

if Computer == player:
    print("Draw")
elif Computer == 0:
    if player == 1:
        player_score += 1
        print("Player Wins")
    else:
        computer_score += 1
        print("Computer Wins")
elif Computer == 1:
    if player == 0:
        computer_score += 1
        print("Computer wins")
    else:
        player_score += 1
        print("Player wins")
else:
    if player == 0:
        player_score += 1
        print("Player wins")
    else:
        computer_score += 1
        print("Computer wins")

print(f"Player Score: {player_score}\nComputer Score: {computer_score}")
