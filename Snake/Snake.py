from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(5, 0)]
aim = vector(0, -5)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -100 < head.x < 90 and -100 < head.y < 90

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 4, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-7.5, 7.5) * 10
        food.y = randrange(-7.5, 7.5) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 4, 'black')

    square(food.x, food.y, 4, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
move()
done()