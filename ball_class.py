from turtle import Turtle
import random


class Ball():
    def __init__(self):
        self.ball_obj = self.creat_ball()
        self.move_the_ball()



    def creat_ball(self):
        ball_obj = Turtle()
        ball_obj.color("white")
        ball_obj.shape("circle")
        ball_obj.shapesize(1)
        ball_obj.penup()
        ball_obj.speed(0)
        return ball_obj

    def move_the_ball(self):
        temp = random.randint(-89,89)
        self.ball_obj.setheading(temp)

    def get_angle(current_angle):
        return 360 - current_angle
    