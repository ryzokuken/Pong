import paddle

class AIPaddle(paddle.Paddle):

    def __init__(self, color, x, y, ball, speed):
        super().__init__(color, x, y)
        self.ball = ball
        self.speed = speed

    def update(self):
        x, y = self.ball.rect.center
        if x > 400:
            ownx, owny = self.rect.center
            ydiff = owny - y
            if abs(ydiff) <= self.speed:
                self.rect.center = (ownx, y)
            elif ydiff > 0:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
