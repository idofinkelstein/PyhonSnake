import random
from turtle import Turtle
from snake import Snake


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__("circle")
        self.color("blue")
        self.penup()
        self.setposition(60, 60)
        self.max_width = screen_width // 2
        self.max_height = screen_height // 2

    def redraw(self, snake: Snake) -> None:
        new_x = random.randrange(-self.max_width, self.max_height, 20)
        new_y = random.randrange(-self.max_height, self.max_height, 20)

        x_range = [x.xcor() for x in snake.snake_body]
        y_range = [y.ycor() for y in snake.snake_body]

        if new_x not in x_range and new_y not in y_range:
            self.goto(new_x, new_y)

