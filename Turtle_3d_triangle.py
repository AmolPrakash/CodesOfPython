from turtle import *
speed(100)
colors = ['red','blue', 'green','yellow']
for i in range(200):
    pencolor(colors[i%3])
    forward(200)
    left(90)
    forward(200)
    left(135)
    x=((2*(200)**2)**0.5)-1
    forward (x)
    right(136)
##    left(22.5)
##    forward(33)
##    right(22.5)
##    
