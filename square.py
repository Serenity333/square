#module to draw a square with a Turtle. WARNING: Does NOT include the Turtle setup

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
