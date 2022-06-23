from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_num=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
         self.write(f"The Score is {self.score_num}", align = "center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score_num+=1
        self.clear()
        self.update_score()