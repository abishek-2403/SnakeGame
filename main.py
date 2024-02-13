from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


is_game_on = True
sleep_speed = 0.08
# snake direction

user_input = screen.textinput(title="Welcome to Snake Game", prompt="What would you like to do? play/exit").lower()
if user_input == "play":
    while is_game_on:
        screen.update()
        time.sleep(sleep_speed)
        snake.move()

        screen.listen()
        screen.onkey(fun=snake.go_up, key="w")
        screen.onkey(fun=snake.go_down, key="s")
        screen.onkey(fun=snake.turn_left, key="a")
        screen.onkey(fun=snake.turn_right, key="d")

        if snake.head.distance(food) < 15:
            food.random_food()
            score.update_score()
            snake.extend()
            sleep_speed -= 0.0001


        # detect collision with wall

        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
            score.reset_score()
            snake.reset_snake()
        # detect collision with tail

        for i in snake.segments[1:]:
            if snake.head.distance(i) < 10:
                score.reset_score()
                snake.reset_snake()

elif user_input == "exit":
    is_game_on = False

screen.exitonclick()
