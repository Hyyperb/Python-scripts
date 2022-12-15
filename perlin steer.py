import random
import turtle
import time

t = turtle.Turtle()
t.speed(100)

d = 5
m = 30

while True:
    a = random.randint(-m,m)
    t.forward(d)
    t.left(a)
    time.sleep(0.05)