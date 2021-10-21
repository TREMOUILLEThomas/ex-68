from turtle import *
def triangle(a):
	begin_fill()
	for i in range (3):
		forward(a)
		left(120)
	end_fill()
a=int(input("cote"))
triangle(a)
forward(100)
triangle(a)
left(120)
forward(a)
left(60)
back(a)
right(60)
triangle(a)
input()