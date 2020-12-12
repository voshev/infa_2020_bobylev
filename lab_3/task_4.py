import turtle

turtle.shape('turtle')


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v_x = 1
        self.v_y = 0
        self.a_y = -0.5

    def jump(self):
        self.v_y = 10

    def move(self):
        self.x += self.v_x
        self.v_y += self.a_y
        self.y += self.v_y
        turtle.goto(self.x, self.y)
        if self.y < 0:
            self.jump()


ball_1 = Ball()
while True:
    ball_1.move()
