from turtle import *
def triangle(a):
	begin_fill()
	for i in range (3):
		forward(a)
		left(120)
	end_fill()
a=int(input("cote"))
triangle(a)
forward(a)
triangle(a)
right(90)
forward((a**2-(a/2)**2)**(0.5))
right(90)
forward(a/2)
left(180)
triangle(a)
	
input()
