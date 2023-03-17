from turtle import Screen
from person import Person
from car import Car
import time
# Make a screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

# Make a turtle and allow him to move up
person = Person(0,0)

# detect if the turtle crosses the line

# create random cars moving from right to left
car = Car(300,20,"purple")
car2 = Car(300,0)
Car(320,-20, "Green")

# detect cars collision with turtle


# screen events
screen.listen()
screen.onkey(person.move, 'Up')

game_is_on = True
while game_is_on:
    car.move()
    car2.move()
    time.sleep(0.1)
    car.check_collision(person.xcor(),person.ycor())
    car2.check_collision(person.xcor(),person.ycor())
    screen.update()


screen.exitonclick()

