import turtle
import another_module

print(another_module.another_variable)

timmy = turtle.Turtle()
print(timmy)
timmy.color("red"), timmy.shape("turtle"), timmy.width(5)
timmy.forward(100), timmy.left(120), timmy.forward(100), timmy.left(120), timmy.forward(100)
timmy.home()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)


my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

