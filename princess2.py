import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For Aditi 👑")
screen.setup(width=800, height=600)

# Draw heart in center
def draw_heart():
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.color("red")
    heart.penup()
    heart.goto(0, -100)
    heart.pendown()
    heart.begin_fill()
    heart.setheading(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

# Draw cartoonish cat
def draw_cat():
    cat = turtle.Turtle()
    cat.hideturtle()
    cat.pensize(3)
    cat.color("white")
    cat.speed(0)

    # Head
    cat.penup()
    cat.goto(200, -50)
    cat.pendown()
    cat.circle(40)

    # Eyes
    for eye_x in [185, 215]:
        cat.penup()
        cat.goto(eye_x, -15)
        cat.pendown()
        cat.begin_fill()
        cat.circle(5)
        cat.end_fill()

    # Ears
    cat.penup()
    cat.goto(175, 0)
    cat.pendown()
    cat.goto(165, 40)
    cat.goto(190, 20)

    cat.penup()
    cat.goto(225, 0)
    cat.pendown()
    cat.goto(235, 40)
    cat.goto(210, 20)

    # Whiskers
    for y in [-25, -20, -15]:
        cat.penup()
        cat.goto(160, y)
        cat.pendown()
        cat.goto(180, y)
        cat.penup()
        cat.goto(240, y)
        cat.pendown()
        cat.goto(220, y)

    # Body
    cat.penup()
    cat.goto(200, -90)
    cat.pendown()
    cat.circle(20)

# Floating love messages
def float_texts():
    for _ in range(120):
        msg = turtle.Turtle()
        msg.hideturtle()
        msg.penup()
        msg.color("dark red")
        x = random.randint(-390, 390)
        y = random.randint(-280, 280)
        msg.goto(x, y)
        msg.write("I love you princess", align="center", font=("Arial", 10, "bold"))
        time.sleep(0.01)

# Run sequence
draw_heart()
time.sleep(0.5)
draw_cat()
time.sleep(0.5)
float_texts()

turtle.done()
