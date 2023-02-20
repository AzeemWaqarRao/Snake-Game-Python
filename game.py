# Object Oriented Approach of working with turlte

import turtle
import random

WIDTH = 600
HEIGHT = 600
DELAY = 150
FOOD_SIZE = 10
SCORE = 0
offsets = {
    "up": (0,20),
    "right": (20,0),
    "down": (0,-20),
    "left": (-20,0)
}

# HELPER FUNCTIONS
def reset():
    global SCORE, snake, snake_direction, food_pos
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    SCORE = 0
    snake = [[0,0], [20,0], [40,0], [60,0]]
    snake_direction = "up"
    move_snake()

def set_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def set_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def set_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def set_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def get_distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def get_random_food_pos():
    x = random.randint(-WIDTH/2 + FOOD_SIZE, +WIDTH/2 - FOOD_SIZE)
    y = random.randint(-HEIGHT/2 + FOOD_SIZE, +HEIGHT/2 - FOOD_SIZE)
    return (x,y)


def check_collisions():
    global food_pos , SCORE
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        SCORE += 1
        food.goto(food_pos)
        return True
    return False

def move_snake():
    stamper.clearstamps()
    # updating head of snake
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check Collisions
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 \
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
        reset()

    else:
        snake.append(new_head)

        # Check food collision
        if not check_collisions():
            # if there's no collision then we will pop else size will increase
            snake.pop(0)

        # Printing snake
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Update screen
        screen.title(f"Score is : {SCORE}")
        screen.update()
        turtle.ontimer(move_snake,DELAY)



# Create turtle object
stamper = turtle.Turtle()
stamper.color('red')
stamper.shape('square')
stamper.shapesize(15/20)
stamper.penup()

# Creating Food
food = turtle.Turtle()
food.color('green')
food.shape('circle')
food.shapesize(FOOD_SIZE/20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Creating screen
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

# Event Handler
screen.listen()
screen.onkey(set_up, "Up")
screen.onkey(set_down, "Down")
screen.onkey(set_left, "Left")
screen.onkey(set_right, "Right")

reset()

# Ending the program
turtle.done()