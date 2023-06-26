import turtle
import time
turtle.shape('turtle')
way = 400
turtle.speed(1000)

def draw_kantors(l, n, x=0, y=0):
    dist = l / 3
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        return

    elif n >= 1:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        draw_kantors(dist, n - 1, x, y - 20)
        draw_kantors(dist, n - 1, x + dist * 2, y - 20)

draw_kantors(way, 15, x=-way / 2)

time.sleep(40)