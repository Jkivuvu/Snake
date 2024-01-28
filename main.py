import turtle
import time
from snake import Snake
from Food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

Game_is_on = True
while Game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if snake.snakes[0].distance(food) < 15:
        score.Scores()
        snake.extend()
        food.refresh()

    if snake.snakes[0].xcor() > 285 or snake.snakes[0].xcor() < -285 or snake.snakes[0].ycor() > 285 or snake.snakes[
        0].ycor() < -285:
        food.refresh()
        score.reset()
        score.current_score()
        snake.snake_reset()
        snake.snakes[0].goto(0, 0)
        #Game_is_on = False

    for sn in snake.snakes[1:]:
        if snake.snakes[0].distance(sn) < 10:
            food.refresh()
            score.reset()
            score.current_score()
            snake.snake_reset()
            snake.snakes[0].goto(0, 0)
            #Game_is_on = False


screen.exitonclick()
