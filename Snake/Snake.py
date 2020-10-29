from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(30, 0)]
aim = vector(0, -30)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -150 < head.x < 150 and -180 < head.y < 160

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'blue')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-35, 35) * 10
        food.y = randrange(-35, 35) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 29, 'red')

    square(food.x, food.y, 29, 'magenta')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(30, 0), 'Right')
onkey(lambda: change(-30, 0), 'Left')
onkey(lambda: change(0, 30), 'Up')
onkey(lambda: change(0, -30), 'Down')
move()
done()