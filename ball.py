import pygame
import random
import math

import block
import colors

random.seed()

def random_speed(t):
  x = random.random() * t
  y = math.sqrt(math.pow(t, 2) - math.pow(x, 2))
  if x < t/2:
    return random_speed(t)
  return (x, y)

class Ball(block.Block):
  def __init__(self, color, x, y, speed, player_score, computer_score):
    super().__init__(colors.WHITE, x, y, 20, 20)
    self.image.set_colorkey(colors.WHITE)
    pygame.draw.circle(self.image, color, [10, 10], 10)

    self.initial_speed = speed
    self.set_random_speed(speed)

    self.player_score = player_score
    self.computer_score = computer_score

  def increase_speed(self, value):
    if self.speed_x > 0:
      self.speed_x += value
    else:
      self.speed_x -= value

  def set_random_speed(self, speed):
    self.speed_x, self.speed_y = random_speed(speed)
  
  def reset_speed(self):
    self.set_random_speed(self.initial_speed)

  def update(self):
    self.rect.x += self.speed_x
    self.rect.y += self.speed_y

    if self.rect.top < 0 or self.rect.bottom > 600:
      self.speed_y = -self.speed_y
    if self.rect.left < 0:
      self.computer_score()
      self.rect.center = (400, 300)
      self.reset_speed()
    if self.rect.right > 800:
      self.player_score()
      self.rect.center = (400, 300)
      self.reset_speed()