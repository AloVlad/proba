import turtle

turtle.shape('turtle')
turtle.speed(5)

def one():
    turtle.left(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)


def otstup():
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()


def chet():
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(20)
    turtle.left(180)
    turtle.right(90)


def sem():
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(40)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)


def nol():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)


A = [one(), otstup(), chet(), otstup(), one(), otstup(), sem(), otstup(), nol(), otstup(), otstup(), nol()]
