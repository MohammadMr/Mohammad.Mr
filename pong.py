from turtle import Screen,Turtle
from Stick_class import stick
from screen_class import pong_screen
from ball_class import Ball
import time
import random
# def out_of_boundaries(ball):
#     # Up
#     ball.


    # Down
    # if 


def check_status(ball_obj,left_stick,right_stick):
    '''
    0 --> top or bottom\n
    1 --> player score\n
    2 --> opponent score\n
    3 --> is on one of the sticks
    '''
    
    if ball_obj.pos()[1]>= 290 or ball_obj.pos()[1]<= -280:
        return 0
    if  ball_obj.pos()[0]>= 290:
        return 2
    if ball_obj.pos()[0]<= -290:
        return 1
    for item in left_stick.stick_man:
        if ball_obj.distance(item)< 15:
            return 3
    for item in right_stick.stick_man:
        if ball_obj.distance(item)< 15:
            return 3
    # for item in left_stick.stick_man:
    #     if item.pos()

def get_angle(ball_obj,status):
    head = ball_obj.heading()
    if head == 0 or head == 180 and ball_obj.pos()[0] >0:
        return random.randint(90,170)
    if head == 0 or head == 180 and ball_obj.pos()[0] <0:
        return random.randint(-90,90)
    if status == 3:
        if head >= 270 :
            temp = abs(360-head)
            return 180 + temp
        else:
            return 180-ball_obj.heading()
    else:
        return 360-ball_obj.heading()

screen = pong_screen()
right_stick = stick((280,0))
left_stick=stick((-280,0))
ball = Ball()
print(ball.ball_obj.heading())


right_stick.stick_man[0].color("red")

# screen.screen.update()

# move the stick

screen.screen.listen(280,280)

screen.screen.onkeypress(right_stick.move_up , "w")
screen.screen.onkeypress(right_stick.move_down , "s")

screen.screen.onkeypress(left_stick.move_up , "Up")
screen.screen.onkeypress(left_stick.move_down , "Down")
end_of_game = False
# ball.ball_obj.setheading(20)
# ball.ball_obj.goto(100,10)
counter = 0
while not end_of_game:
    screen.screen.update()
    ball.ball_obj.forward(10)
    status = check_status(ball.ball_obj,left_stick,right_stick)
    if status == 0:
        ball.ball_obj.setheading(get_angle(ball.ball_obj,status))
    elif status == 1:
        print("you get a point")
        end_of_game = True
    elif status == 2:
        print('you lost a point')
        end_of_game = True
    elif status == 3:
        ball.ball_obj.setheading(get_angle(ball.ball_obj,status))
        counter+=1

    print(ball.ball_obj.pos(),"\n")
    print(right_stick.stick_man[0].pos(),"\n")
    print(ball.ball_obj.heading())
    
    print(counter,'\n')
    time.sleep(0.091)





screen.screen.exitonclick()