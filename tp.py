from turtle import *
import random

t=Turtle()
t.getscreen().bgcolor('black')
#t.getscreen().screensize(1000,1000)
t.speed(0)
#t.setpos(600,600)

x=1

while x < 400:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    colormode(255)
    t.pencolor(r,g,b)

    t.fd(50 + x)
    t.rt(90.991)

    x=x+1




t.getscreen().mainloop()