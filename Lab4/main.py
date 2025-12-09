import turtle
import random

#PUT FUNCTIONS HERE
def draw_pumkin(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()

    t.fillcolor("#8f4c00")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

    #stem
    t.goto(x - 10, y + radius)
    t.pendown()
    t.fillcolor("#007311")
    t.begin_fill()
    for i in range(4):
        t.forward(radius // 5)
        t.left(90)
        t.forward(radius // 2)
        t.left(90)
    t.end_fill()

    draw_mouth(t, (x - radius) + 50, y - (radius * 0.5), radius / 0.8)
    draw_eye(t, (x - radius) + 30, y + (radius * 0.3), radius // 5)

def draw_mouth(t, x, y, width):
    # t.setheading(60)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#CBCE11")
    t.begin_fill()
    t.right(60)
    for _ in range(5):

        # t.speed(1)
        t.forward(width // 6) #Defines how much angle the teeth have: bigger number = smaller teeth
        t.left(120)
        t.forward(width // 6) 
        t.right(120)
    t.end_fill()
    t.left(60)

#def draw_eye(t, x, y, size): 
    """Draws one triangular eye at the given (x, y) position."""
    """t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, [(x, y), (x + size, y), (x + size / 2, y + size)], 3)
    t.end_fill()"""

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_polygon(t, sides, length):
    angle = 360 / sides
    print("angle", angle)
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_sky(t, stars):
    for _ in range(stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

t = turtle.Turtle()
t.speed(10)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("#043b39")
screen.setup(width=600, height=600)

t.clear()

for i in range(3):
    print(i)
    #draw_pumkin(t, i, 0, 50)
draw_pumkin(t, 100, -200, 100)
draw_pumkin(t, -50, -200, 80)
draw_sky(t, 20)
turtle.exitonclick()