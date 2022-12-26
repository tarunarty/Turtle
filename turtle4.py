import turtle
import math
turt = turtle.Turtle()
turtle.bgcolor("black")
turt.color("white","cyan")
def star(turt,size):
    turt.begin_fill()

    for i in range(5):
        turt.forward(size)
        turt.right(216)
    turt.end_fill()
    turt.forward(size)
    turt.right(72)
    
for j in range(5):
    star(turt,200)

dist1 = 400*(math.sin(math.radians(18)))
turt.up()
turt.right(36)
turt.forward(dist1)
turt.right(72)
turt.down()
dist2 = 2*(400 - 400*(math.cos(math.radians(36))))*(math.cos(math.radians(36)))
star(turt,dist2)
turtle.done()
