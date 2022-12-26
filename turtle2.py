import turtle
turt = turtle.Turtle()
turtle.bgcolor("black")
turt.color("white" , "cyan")
def star(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(216)
size = int(input())
turt.begin_fill()
star(turt,size)
turt.end_fill()
