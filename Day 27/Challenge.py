def add(*args):
    y = 0
    for x in args:
        y += x

    return y


print(add(3, 4, 5, 6, 7))


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R", seats=4)
print(my_car.seats, my_car.color)

