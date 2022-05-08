from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y= self.ycor()+self.y_move
        self.penup()
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()




