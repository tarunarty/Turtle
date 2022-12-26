import turtle
turtle.bgcolor("black")
turt = turtle.Turtle()
turt.color("cyan" , "orange")
turt.width(5)
def triangle(turt):
    turt.begin_fill()
    for i in range(3):
        turt.forward(60)
        turt.right(120)
    turt.end_fill()
    turt.left(120)
turt.speed(0)

for i in range(60):
    turt.forward(150)
    turt.right(18)
    triangle(turt)
turtle.done()
