from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Arial", 80, "normal"))
        
    def add_lscore(self):
        self.lscore += 1
    
    def add_rscore(self):
        self.rscore += 1