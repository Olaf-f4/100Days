fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    if index > len(fruits) - 1:
        raise IndexError("Outside of Scope")
    else:
        fruit = fruits[index]
        print(fruit + " pie")


# 🚨 Do not change the code below
make_pie(2)


