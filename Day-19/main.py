from turtle import Turtle, Screen

screen = Screen()
screen.setup(1200, 800)
user_guess = screen.textinput("Make your bet!", "Who's going to win? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-580, y_positions[turtle_index])

screen.exitonclick()
