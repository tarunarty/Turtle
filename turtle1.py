import turtle
turt = turtle.Turtle()
turtle.bgcolor("black")
turt.color("orange" , "cyan")
def flower(turt):
    turt.begin_fill()
    turt.speed(0)
    for i in range(72):
        turt.forward(400)
        turt.left(175)
    i = 0
    turt.end_fill()
for i in range(3):
    flower(turt)
    turt.left(120)

