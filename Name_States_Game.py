from turtle import Turtle , Screen
import time
turtle = Turtle()
screen = Screen()
image = "India_Map.gif"
screen.addshape(image)
turtle.shape(image)


states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
states_coordinates = [
    (-78.0, -155.0),
    (220.0, 114.0),
    (157.0, 73.0),
    (45.0, 57.0),
    (-30.0, -61.0),
    (-164.0, -147.0),
    (-227.0, 1.0),
    (-141.0, 137.0),
    (-89.0, 189.0),
    (19.0, 27.0),
    (-154.0, -164.0),
    (-128.0, -228.0),
    (-138.0, 1.0),
    (-179.0, -83.0),
    (198.0, 37.0),
    (138.0, 54.0),
    (181.0, 10.0),
    (211.0, 61.0),
    (-2.0, -46.0),
    (-160.0, 162.0),
    (-236.0, 88.0),
    (102.0, 98.0),
    (-104.0, -231.0),
    (-94.0, -94.0),
    (161.0, 21.0),
    (-72.0, 106.0),
    (-69.0, 162.0),
    (71.0, 9.0)
]

score = 0
states_guessed = []
not_guessed=[]
def states_not_guessed():
    for i in range(len(states)):
        if states[i] not in states_guessed:
            not_guessed.append(states[i])
    print(f"States Not guessed: {not_guessed}")

for i in range (30):
    ans_state = screen.textinput(title = f" {score}/28 Answered Correctlt\n Guess the state", prompt = "What's another state's name")
    if (ans_state == "end"):
        states_not_guessed()
        break
    for u in range(len(states)):
        if states[u].lower() == ans_state.lower() :
            states_guessed.append(states[u])
            index = u
            pen = Turtle()
            pen.up()
            pen.color("firebrick")
            pen.goto(states_coordinates[u])
            pen.write(f"{states[u]}",font=("Arial", 10, "bold"))
            score += 1








screen.exitonclick()
