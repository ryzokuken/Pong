import pygame
import block

class Paddle(block.Block):
  def __init__(self, color, x, y):
    super().__init__(color, x, y, 20, 100)

  def move(self, d):
    f = self.rect.y + d
    if f >= 0 and f <= 500:
      self.rect.y = f