from turtle import Turtle


class Snake:
    SNAKE_INITIAL_POSITION = ((0, 0), (-20, 0), (-40, 0))
    DISTANCE = 20

    def __init__(self):
        self.max_x = None
        self.max_y = None
        self.snake_body: list[Turtle] = []
        for position in Snake.SNAKE_INITIAL_POSITION:
            self.add_segment(position)
        self.head = self.snake_body[0]

    def add_segment(self, position) -> None:
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.setposition(position)
        # segment.speed(0.05)
        self.snake_body.append(segment)

    def move(self) -> None:
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(Snake.DISTANCE)
        if self.max_x and self.max_y:
            if self.head.xcor() > self.max_x:
                self.head.setposition(-self.max_x, self.head.ycor())
            elif self.head.xcor() < -self.max_x:
                self.head.setposition(self.max_x, self.head.ycor())
            if self.head.ycor() > self.max_y:
                self.head.setposition(self.head.xcor(), -self.max_y)
            elif self.head.ycor() < -self.max_y:
                self.head.setposition(self.head.xcor(), self.max_y)

    def extend(self) -> None:
        self.add_segment(self.snake_body[-1].pos())

    def bound_to_screen(self, width, height) -> None:
        self.max_x = width // 2
        self.max_y = height // 2

    def right(self) -> None:
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)

    def left(self) -> None:
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)

    def up(self) -> None:
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)
