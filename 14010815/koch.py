import turtle
t = turtle.Turtle()
t.speed(0)

def koch(x, d):
    if d==0:
        return

    koch(x, d-1)
    t.fd(x)
    t.lt(60)
    koch(x, d-1)
    t.fd(x)
    t.rt(120)
    koch(x, d-1)
    t.fd(x)
    t.lt(60)
    koch(x, d-1)
    # t.fd(x)

def draw(x, d):
    for i in range(3):
        koch(x/3**d, d)
        t.fd(x/3**d)
        t.rt(120)

# the following is to adjust the picture in the middle of screen.
t.penup()
t.bk(350)
t.lt(90)
t.fd(200)
t.rt(90)
t.pendown()

draw(650, 4)
turtle.mainloop()
