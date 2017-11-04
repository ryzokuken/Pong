import pygame
import colors

class Text(pygame.sprite.Sprite):
  def __init__(self, font, text, x):
    super().__init__()
    self.font = font
    self.x = x
    self.update_text(text)

  def update_text(self, text):
    self.image = self.font.render(str(text), True, colors.WHITE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, 300)