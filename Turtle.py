import turtle
import random

t = turtle.Turtle()
t.speed(30)
t.setpos(-288,250)
t.clear()

a = 0
h = 4
x,y = t.pos()

def test(h,samples):
	y = 0
	for i in range(samples):
		y += random.randint(-h,h)
	return y

for _ in range(5):
    t.penup()
    y -= 80
    x = -288
    t.setpos(x,y)
    t.pendown()
    for _ in range(500):
        t.setpos(x,y)
        x += 1
        y += random.randint(-h,h)
    
    
    
