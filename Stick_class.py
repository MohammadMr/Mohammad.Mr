from turtle import Turtle


class stick():
    def __init__(self,pos):
        self.stick_man = []
        self.create_stick(pos)


    def create_stick(self,pos):
        for i in range(3):
            temp = Turtle()
            temp.color("white")
            temp.shape("square")
            temp.shapesize(1)
            temp.penup()
            temp.speed(0)
            temp.goto(pos)
            temp.setheading(90)
            self.stick_man.append(temp)
        for index ,item in enumerate(self.stick_man):
            self.set_to_down(item,index)


    def set_to_down(self, item,index):
        margin = index * 20
        item.backward(margin)

    def move_up(self):
        if self.stick_man[0].pos()[1] < 290:
            for item in self.stick_man:
                item.forward(10)

    def move_down(self):
        # self.stick_man.reverse()
        if self.stick_man[-1].pos()[1] > -280:
            for item in self.stick_man:
                item.backward(10)
        


    