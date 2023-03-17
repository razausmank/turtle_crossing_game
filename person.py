from turtle import Turtle

class Person(Turtle):
    def __init__(self, x_position=0 , y_position=-280):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(x_position, y_position)

    def move(self):
        self.forward(20)
