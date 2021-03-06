#Simple test to learn how to use the "turtle.circle" method
#Alejandro Morfin Sepulveda
#Fatima Mourino Rosendo
#Miguel Angel Flores Alvarez
#30/10/20

#Complete
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Modify the range
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Modify the value of the range and degrees, divide in the circle in the number of sections wanted
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Modify the value of the range and degrees
    for count in range(4):
        forward(end.x - start.x)
        left(90)
        
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Modify the value of the range and degrees
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Modify the colours and represent it with the first letter of the each one
onkey(lambda: color('cyan'), 'C')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('blue'), 'T')
onkey(lambda: color('black'), 'B')
onkey(lambda: color('green'), 'G')
#Modify the shape and represent it with the fisrt letter of each one
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()