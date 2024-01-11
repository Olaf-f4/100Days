import string
string.ascii_lowercase
alphabet = list(string.ascii_lowercase)
# Caesar Cipher


def encrypt(message):
    encryption = ""
    for x in message:
        position = alphabet.index(x) + 6
        encryption += alphabet[position]
    return encryption


def decrypt(code):
    decryption = ""
    for x in code:
        position = alphabet.index(x) - 6
        decryption += alphabet[position]
    print(decryption)


user_Input = input("Enter thing here. ").lower()

encrypt(user_Input)
y = encrypt(user_Input)
decrypt(y)

# Better prime calculator


def prime_checker2(z):
    is_prime = True
    for i in range(2, z):
        if z % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


z = int(input())
prime_checker2(z)

# Prime Number Calculator


def prime_checker(n):
    for x in prime_numbers:
        if x == n:
            print("It is a prime number")
            break
    else:
        print("Not a prime number")


prime_numbers = ('''2  3	5	7	11	13	17	19	23
                 29	31	37	41	43	47	53	59	61
                 67	71	73	79	83	89	97	101	103
                 107	109	113	127	131	137	139	149	151
                 157	163	167	173	179	181	191	193	197''').split()

print(prime_numbers)
print(type(prime_numbers))
n = input()  # Check this number
prime_checker(n)

# Paint Area Calculator
import math


def paint_calc(x, y, z):
    number_of_cans = math.ceil((x*y) / z)
    print(f"You'll need {number_of_cans} cans.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(test_h, test_w, coverage)


def greet(x):
    print("Hello")
    print("How are you")
    print("Buenos Dias")
    if x == 1:
        print("Great! It is correct")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}")


user_Input = input("Enter your name here: ")
greet_with_name(user_Input)

# Functions with more than 1 input


def greet_with(name, location):
    print(f"Hello {name}, you are from {location}! I used to live there! Beautiful place.")


user_Input_two = input("What's your name? ")
user_Input_three = input("Where are you from? ")

greet_with(user_Input_two, user_Input_three)