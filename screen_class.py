from turtle import Screen,Turtle

class pong_screen():
    def __init__(self):
        self.screen = Screen()
        self.creat_screen()

    def creat_screen(self):
        self.screen.setup(height= 600 , width= 600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")  
        self.screen.tracer(0)
        self.screen.listen()
     