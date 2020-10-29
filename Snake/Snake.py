from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(100, 0)]
aim = vector(0, -100)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -2000 < head.x < 1900 and -2000 < head.y < 1900

def move():
    "Move snake forward one segment."
    head = snake[-10].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 90, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-150, 150) * 100
        food.y = randrange(-150, 150) * 100
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 90, 'black')

    square(food.x, food.y, 90, 'green')
    update()
    ontimer(move, 1000)

setup(4200, 4200, 3700, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(100, 0), 'Right')
onkey(lambda: change(-100, 0), 'Left')
onkey(lambda: change(0, 100), 'Up')
onkey(lambda: change(0, -100), 'Down')
move()
done()