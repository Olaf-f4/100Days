import pandas
import turtle

screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)

# print(data["Florida"].to_list)

# Need User Input
# if user input == "" on list
# Then make turtle named x
# Send it to relevant spot on map

game = True
while game:
    user_input = turtle.textinput("States", "Name the States")

    # Chicago = data[data["state"] == "chicago"]

    if user_input in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    else:
        pass

screen.exitonclick()
