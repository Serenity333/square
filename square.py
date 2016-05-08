#module to draw a square with a Turtle. Includes Turtle setup
import turtle

t = turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)
