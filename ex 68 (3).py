from turtle import *
def triangle(a):
    begin_fill()
    for i in range (3):
        forward(a)
        left(120)
    end_fill()
def tritri(a):
    for i in range(3):
        triangle(a)
        left(90)
        up()
        forward(a/2)
        right(90)
        forward(a/6)
        down()
        a=a*(2/3)
        if i == 7:
            a=100
a=int(input("cote"))
tritri(a)
hideturtle()
input()
