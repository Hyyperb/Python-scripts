import turtle

#supposed to draw 69, yet to finish (this means i won't do this)

t = turtle.Turtle()
t.speed = 30
t.penup()
t.setpos(0,100)
t.setheading(180)
t.pendown()

d = 2
a = 160
unit = 0.5

while a < 550:
    t.left(1)
    if a < 250:
        d = 2*unit
    elif a <270:
        d += 0.1*unit
    elif a <290:
        d = 10*unit
    elif a < 500:
        d = 2*unit
    t.forward(d)
    a+=1

t.penup()


t.setpos(0,100)
    
    
    