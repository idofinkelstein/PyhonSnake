import sys
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.tracer(0)

snake = Snake()
food = Food(560, 560)
scoreboard = ScoreBoard()
snake.bound_to_screen(540, 540)

screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def main():
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 15:

                scoreboard.game_over()
                game_is_on = False
                break

        if snake.head.distance(food) < 20:

            food.redraw(snake)
            scoreboard.update_score()
            snake.extend()

    screen.exitonclick()


if __name__ == '__main__':
    main()
