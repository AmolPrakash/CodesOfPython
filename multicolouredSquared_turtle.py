from turtle import *
from random import *

colours=['red', 'blue', 'green', 'orange','purple']
speed(0)
for i in range(350,0, -1):
    shuffle(colours)
    pencolor(colours[0])
    forward(100)
    right(90)
    
    right(22.5)
    forward(5)
    left(22.5)
    
