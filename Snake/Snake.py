#Simple test to learn how to use the "turtle.circle" method
#Alejandro Morfin Sepulveda
#Fatima Mourino Rosendo
#Miguel Angel Flores Alvarez
#30/10/20

from turtle import *
from random import randrange
from freegames import square, vector
#Defining where is situated all of the components
#Modify the x value in snake
#Change the y value in aim
food = vector(0, 0)
snake = [vector(5, 0)]
aim = vector(0, -5)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    #Amend the value and the colour 
    if not inside(head) or head in snake:
        square(head.x, head.y, 4, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
    #Recast the x and y values of the vector
        food.x = randrange(-7, 7) * 10
        food.y = randrange(-7, 7) * 10
    else:
        snake.pop(0)

    clear()
#Change the body color of the snake and the value previously granted
    for body in snake:
        square(body.x, body.y, 4, 'black')
#Change the food color and the value previously granted
    square(food.x, food.y, 4, 'green')
    update()
    ontimer(move, 50)

setup(210, 210, 185, 0)
hideturtle()
tracer(False)
listen()
#Defining the directions of the snake
#Change the value in change(x,y)
#In the directions right and left change the x value
#In the directions up and down change the y value 
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
move()
done()