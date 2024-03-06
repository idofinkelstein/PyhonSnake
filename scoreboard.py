from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("highest_score.txt", "r") as f:
                self.highest_score = int(f.read())
        except FileNotFoundError:
            self.highest_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.display_score()
        self.hideturtle()

    def increment(self) -> None:
        self.score += 1
        if self.score >= self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as f:
                f.write(str(self.highest_score))

    def update_score(self) -> None:
        self.increment()
        self.clear()
        self.display_score()

    def display_score(self) -> None:
        self.write(f"Your Score: {self.score} Highest Score: {self.highest_score}", align="center",
                   font=("italic", 24, "normal"))

    @staticmethod
    def game_over() -> None:
        game_over = Turtle()
        game_over.penup()
        game_over.color("red")
        game_over.write(f"GAME OVER", align="center", font=("italic", 30, "normal"))
