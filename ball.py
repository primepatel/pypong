from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
    
    def move(self):
        cords = self.xcor()+10, self.ycor()+10
        self.goto(cords)