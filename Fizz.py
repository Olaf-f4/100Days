numbers = 1
while numbers <= 100:
    numbers += 1

    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)

for i in range(1, 101):
    print(i)
