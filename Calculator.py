logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Add
def add(n1, n2):
    return n1 + n2


def subtract(a1, a2):
    return a1 - a2


def multiply(m1, m2):
    return m1 * m2


def divide(z1, z2):
    return z1 / z2


# Keys = +-*/
# Terms = value

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
# function = operations["+"]
# function(2, 3)

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
how = input("How do you want to mess with the numbers? + - * /")


def solve(d, y, z):
    for x in operations:
        print(x)
        if x == d:
            function = operations[x]
            return function(y, z)


print(solve(how, num1, num2))

# Recursion - calls itself to restart function.
# def calculator():
# if ...
# else:
#    calculator()