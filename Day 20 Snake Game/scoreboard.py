from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_num=0
        
        with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 20 Snake Game/data.txt", mode="r") as file:
            self.high_score= int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"The Score is {self.score_num}, High Score: {self.high_score}" , align = "center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 20 Snake Game/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                
        self.score_num=0    
        self.update_score()

    def increase_score(self):
        self.score_num+=1
        self.update_score()