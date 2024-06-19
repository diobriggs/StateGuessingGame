import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
data = pandas.read_csv("50_states.csv")

while score != 50:
    answer_state = screen.textinput(f"{score}/{len(data)} States Correct", "What's another state's name?")
    correct_state = data[data["state"] == answer_state]

    for state in data.state:
        if state == answer_state:
            state_x = correct_state["x"].values[0]
            state_y = correct_state["y"].values[0]
            t = turtle.Turtle()
            score += 1
            t.penup()
            t.hideturtle()
            t.goto(state_x, state_y)
            t.write(f"{state}", True, align="center")





screen.exitonclick()
