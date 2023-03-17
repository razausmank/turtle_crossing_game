from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, x_position, y_position, color="blue"):
        super().__init__()
        self.shape('square')
        self.setheading(180)
        self.color(color)
        self.len = random.randint(a=1,b=5)
        self.shapesize(stretch_wid=1, stretch_len=self.len)
        self.penup()
        self.goto(x_position, y_position)

    def move(self):
        pass
        self.forward(10)
        # self.check_collision()

    def check_collision(self, x_cor, y_cor):
        pass
        if y_cor == self.ycor() and x_cor > self.xcor() and x_cor < (self.xcor() + ( (self.len - 1 * 20) )):
            print("collision")
