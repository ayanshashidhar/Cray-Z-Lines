import random
import sys
import turtle

# Make sure your compiler can run the Python modules random, sys, and turtle.
# As with the "https://github.com/blackjack2010/Sierpinski-Triangle", the code might not run properly with an online compiler.

def setup():
    sys.setExecutionLimit(600000)
    t.speed(0)


colors = ["black", "blue", "brown", "cyan", "darkgray", "gray", "green", "lightgray", "lime", "magenta", "orange", "pink", "purple", "red", "silver", "white", "yellow"]

def turt():
    global t
    t = turtle.Turtle()

def rand():
    global angle
    color = random.choice(colors)
    t.pencolor(color)
    angle = random.randint(1, 360)
    
    
def draw():
    t.fd(50)
    t.right(angle)
   
turt()
setup() 

while True:
    rand()
    draw()


### Thank you!!!
