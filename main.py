import pygame
import paddle
import ball
import text
import colors

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
done = False

default_font = pygame.font.Font(None, 400)
pygame.mixer.music.load('pong.wav')

speed_ball = 10
speed_player = 10
score_player = 0
score_computer = 0


def scorep():
    global score_player
    global pscore

    score_player += 1
    pscore.update_text(score_player)


def scorec():
    global score_computer
    global cscore

    score_computer += 1
    cscore.update_text(score_computer)


paddles = pygame.sprite.Group()
balls = pygame.sprite.Group()
displays = pygame.sprite.Group()

player = paddle.Paddle(colors.BLUE, 20, 20)
computer = paddle.Paddle(colors.RED, 760, 480)
ball = ball.Ball(colors.GREEN, 390, 290, speed_ball, scorep, scorec)
pscore = text.Text(default_font, '0', 200)
cscore = text.Text(default_font, '0', 600)

paddles.add([player, computer])
balls.add(ball)
displays.add([pscore, cscore])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    k = pygame.key.get_pressed()
    if k[pygame.K_UP]:
        player.move(-speed_player)
    if k[pygame.K_DOWN]:
        player.move(speed_player)

    balls.update()
    computer.rect.y = ball.rect.y - 40
    for p in pygame.sprite.spritecollide(ball, paddles, False):
        ball.speed_x = -ball.speed_x
        ball.increase_speed(1)
        pygame.mixer.music.play()

    screen.fill(colors.BLACK)
    displays.draw(screen)
    pygame.draw.line(screen, colors.WHITE, [400, 0], [400, 600], 3)
    paddles.draw(screen)
    balls.draw(screen)
    pygame.display.flip()

    clock.tick(60)
