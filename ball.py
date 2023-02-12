from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.goto(-100, 250)
        self.y_acceleration = 200
        self.y_velocity = 0
        self.x_velocity = 0
        self.y_move = 0
        self.x_move = 0

    def move(self):
        self.y_velocity = self.y_velocity + 0.04*self.y_acceleration
        self.y_move = self.y_velocity*0.04 + 0.5*self.y_acceleration*0.0016
        self.x_move = self.x_velocity * 0.04
        self.goto(self.xcor()+self.x_move, self.ycor()-self.y_move)

    def bounce(self):
        self.y_velocity = -self.y_velocity

    def reflect(self):
        self.x_velocity = -self.x_velocity
