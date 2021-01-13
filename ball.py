from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        cords = self.xcor() + self.x_move, self.ycor()+ self.y_move
        self.goto(cords)
    
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.95
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x() # to reverse direction
        self.move_speed = 0.1 # reset move speed